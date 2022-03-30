import sys
import time
import os
import crc16
from NJLikeLib.CanCmd import *
from PySide6 import QtWidgets, QtCore
from threading import Thread, Event, Timer
from queue import Queue
from UI import ui_00login, ui_01test, ui_02upgrade, ui_03write
from DB import test, upgrade

# 升级同步事件
update_event = Event()
update_queue_start_cb = Queue()
update_queue_send_cb = Queue()

# 接收线程类
class recv_worker(QtCore.QThread):
    global recv_data
    signal = QtCore.Signal(type(recv_data))
    def __init__(self):
        super().__init__()

    def run(self):
        # global recv_data
        while True:
            # print("recv worker is loop")
            len = pDll.CAN_GetReceiveCount(devHandle, 0)
            if len > 0:
                res = pDll.CAN_ChannelReceive(
                    devHandle, 0, pointer(recv_data), 1, -1)
                # print("get date", res, len)
                if res != CAN_RESULT_ERROR:
                    self.cb_can_receive(recv_data)
                else:
                    pDll.CAN_ClearReceiveBuffer(devHandle, 0)
                    print("recv worker is running")
            # else:
            #     time.sleep(1)
            #     print("recv worker is sleep")

    def cb_can_receive(self, recv_data1):
        # print("cb_can_receive:0x%x" % recv_data1.uID,
        #       "len: ", len(recv_data1.arryData))
        # widget.recv_data_loop(recv_data1)
        self.signal.emit(recv_data1)


# 测试模式保持线程
class test_mode_keepalive(QtCore.QThread):
    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            psend_data = CAN_DataFrame(nSendType=0, bRemoteFlag=0,
                                   bExternFlag=0, nDataLen=8, uID= 0x750)

            for i in range(0, 8):
                psend_data.arryData[i] = 0x00

            res = pDll.CAN_ChannelSend(devHandle, 0, pointer(psend_data), 1)
            if res != CAN_RESULT_ERROR:
                # print("心跳发送成功")
                pass
            else:
                print("心跳发送失败")
            time.sleep(1)


# 升级线程类
class update_worker(QtCore.QThread):
    signal = QtCore.Signal(float)
    err_signal = QtCore.Signal(int)
    def __init__(self):
        super().__init__()

    def run(self):
        global update_event, update_queue_start_cb, update_queue_send_cb, devHandle
        bytes = 6

        # '//'表示向下取整除法
        upgrade.FILE_CNT = upgrade.FILE_SZ//bytes

        if upgrade.FILE_SZ % bytes > 0:
            upgrade.FILE_CNT += 1

        # 都是int型
        # print(type(upgrade.FILE_SZ), type(upgrade.FILE_CNT))
        print("升级包大小：%d"%upgrade.FILE_SZ+"\t升级总包数：%d"%upgrade.FILE_CNT)

        psend_data = CAN_DataFrame(nSendType=0, bRemoteFlag=0,
                                   bExternFlag=0, nDataLen=8, uID= 0x730)

        # 固件大小
        for i in range(0, 4):
            psend_data.arryData[i] = (upgrade.FILE_SZ >> (8*i)) & 0xFF

        # 总包数
        for i in range(0, 2):
            psend_data.arryData[i+4] = (upgrade.FILE_CNT >> (8*i)) & 0xFF

        # CRC16校验
        for i in range(0, 2):
            psend_data.arryData[i+6] = (upgrade.CRC16>> (8*i)) & 0xFF

        # 打印报文
        # for i in range(0, 8):
        #     print( hex(psend_data.arryData[i]), end='\t')

        res = pDll.CAN_ChannelSend(devHandle, 0, pointer(psend_data), 1)
        if res != CAN_RESULT_ERROR:
            print("成功")
        else:
            print("失败")

        data_res = update_queue_start_cb.get()
        # for i in data_res:
        #     print(hex(i))

        if data_res[0] == 0:
            print("允许升级")
            for i in range(0, upgrade.FILE_CNT):
                upgrade.FILE_FD.seek(bytes*upgrade.FILE_CNT)
                # print(upgrade.FILE_FD.read(bytes))

        else:
            print("禁止升级")

        psend_data.uID= 0x732

        for index in range(upgrade.FILE_CNT):
            upgrade.FILE_FD.seek(bytes*index)
            print(hex(index), hex(bytes*index), end='\t')
            # for i in upgrade.FILE_FD.read(bytes):
            #     print(hex(i), end='\t')

            # 初始化
            for i in range(8):
                psend_data.arryData[i] = 0xFF

            # 包索引
            for i in range(0, 2):
                psend_data.arryData[i] = (index >> (8*i)) & 0xFF

            # 数据
            tmp = 2
            for i in upgrade.FILE_FD.read(bytes):
                psend_data.arryData[tmp] = i
                tmp += 1
                # print(hex(upgrade.FILE_FD.read(bytes)[i]), end='\t')

            # for i in psend_data.arryData:
            #     print(hex(i), end='\t')

            # 重试8次
            for i in range(0, 8):
                res = pDll.CAN_ChannelSend(devHandle, 0, pointer(psend_data), 1)
                if res != CAN_RESULT_ERROR:
                    # print("升级包发送成功")

                    # 等待设备回复
                    try:
                        data_res = update_queue_send_cb.get(timeout = 10)
                    except Exception as err:
                        print("异常：%s"%err+"重试次数：%d"%i)
                        continue

                    progress = index/upgrade.FILE_CNT*100
                    if data_res[0] == 0:
                        print("回复成功：",progress)
                        self.signal.emit(progress)
                        if index == upgrade.FILE_CNT-1:
                            self.signal.emit(100)
                            self.err_signal.emit(0)
                            return
                        break
                    else:
                        print("回复失败：")
                        for i in data_res:
                            print(hex(i), end='\t')
                        self.err_signal.emit(-1)
                        # todo: 是否考虑重试3次
                        break
                else:
                    print("升级包发送失败")
                    self.err_signal.emit(-2)
                    break

        f'重试8次依旧失败'
        self.err_signal.emit(-3)



class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.ui = ui_00login.Ui_Form()  # 实例化UI对象
        self.ui.setupUi(self)  # 初始化

        self.init_data()

    def peika_mode(self, mode):
        print(sys._getframe().f_code.co_name, mode)
        # for i in range(len(dwBtr_table[bandRate])):
        #     init_config.dwBtr[i] = dwBtr_table[bandRate][i]
        #     print('0x%x' % init_config.dwBtr[i], type(init_config.dwBtr[i]))
        pass

    def peika_start(self):
        print(sys._getframe().f_code.co_name)
        res_text = self.ui.comboBox.currentText()
        if res_text == "实体卡":
            print("实体卡")
            self.test_mode(1,1)
        if res_text == "模拟卡":
            print("模拟卡")
            self.test_mode(1,2)

    def peika_stop(self):
        print(sys._getframe().f_code.co_name)
        res_text = self.ui.comboBox.currentText()
        if res_text == "实体卡":
            print("实体卡")
            self.test_mode(0,1)
        if res_text == "模拟卡":
            print("模拟卡")
            self.test_mode(0,2)

    # 写SN号
    def writeNumber(self):
        print(sys._getframe().f_code.co_name)
        m_str = self.ui.lineEdit.text()

        msend_data = CAN_DataFrame(
            nSendType=0, bRemoteFlag=0, bExternFlag=0, nDataLen=8)
        msend_data.uID=0x740

        print("第一组")
        # for i in m_str[0:8]:
        #     print(type(i), i, end='\t')

        for i in range(0, 8):
            print(str.encode(m_str[i]), m_str[i], end='\t')
            msend_data.arryData[i] = str.encode(m_str[i])

        res = pDll.CAN_ChannelSend(devHandle, 0, pointer(msend_data), 1)
        if res != CAN_RESULT_ERROR:
            print("成功")
        else:
            print("失败")
            get_error_code(devHandle)

        print("第二组")
        # for i in m_str[8:16]:
        #     print(type(i), i, end='\t')
        print("结束")


        # m_bytes = str.encode(m_str)
        # for i in m_bytes:
        #     print(type(i), i)
        # print(type(m_bytes),m_bytes)

        # for i in range(0, 8):
        #     print(m_bytes[i])

        # # str to bytes
        # str.encode(s)

        # # bytes to str
        # bytes.decode(b)

        # msend_data = CAN_DataFrame(
        #     nSendType=0, bRemoteFlag=0, bExternFlag=0, nDataLen=8, uID=0x740)

        # for i in range(0, 8):
        #     msend_data.arryData[i] = (upgrade.FILE_SZ >> (8*i)) & 0xFF

        # res = pDll.CAN_ChannelSend(devHandle, 0, pointer(msend_data), 1)
        # if res != CAN_RESULT_ERROR:
        #     print("成功")
        # else:
        #     print("失败")
        #     get_error_code(devHandle)

    # 测试接口
    def ceshi_api(self):
        print(sys._getframe().f_code.co_name)
        # self.ui.lb_sn.setText(recv_data.arryData[0])

    # 打开升级文件
    def openBinFile(self):
        print(sys._getframe().f_code.co_name)
        upgrade.FILE_NAME = ""
        # 参数 _ 用于分割第二个返回值，防止 upgrade.FILE_NAME 生成数组
        upgrade.FILE_NAME, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, "选择文件", "", "BIN(*.bin);;All Files(*)")
        self.ui.lb_binpath.setText(upgrade.FILE_NAME)

        upgrade.FILE_SZ = os.path.getsize(upgrade.FILE_NAME)
        print("升级包大小：" + str(upgrade.FILE_SZ), end="\t")
        self.ui.lb_binsize.setText("%d" % upgrade.FILE_SZ+" bytes")

        # 使用open函数打开文件，打开模式选择二进制读取'rb'
        upgrade.FILE_FD = open(upgrade.FILE_NAME, 'rb')

        # CRC16校验
        upgrade.CRC16, key = 0, 0xE32A
        # print(type(upgrade.CRC16))
        for i in upgrade.FILE_FD.read():
            # print(hex(i), end=",")
            upgrade.CRC16 ^= i
            for j in range(8):
                if upgrade.CRC16 & 1 != 0:
                    upgrade.CRC16 = (upgrade.CRC16 >> 1)^key
                else:
                    upgrade.CRC16 = (upgrade.CRC16 >> 1)

        print("upgrade.CRC16: ", upgrade.CRC16, hex(upgrade.CRC16), end='\t')

        # 补齐 CRC
        re_len = upgrade.FILE_SZ % upgrade.BYTES
        if re_len != 0:
            print("最后一包长度：",re_len)
            for i in range(upgrade.BYTES - re_len):
                upgrade.CRC16 ^= 0xFF
                for j in range(8):
                    if upgrade.CRC16 & 1 != 0:
                        upgrade.CRC16 = (upgrade.CRC16 >> 1)^key
                    else:
                        upgrade.CRC16 = (upgrade.CRC16 >> 1)
        print("修正upgrade.CRC16: ", upgrade.CRC16, hex(upgrade.CRC16))



    def upgrade_progress(self, progress):
        # print(sys._getframe().f_code.co_name)
        self.ui.progressBar.setValue(progress)
        speed = progress/100.0*upgrade.FILE_SZ/(time.time() - upgrade.START_TIME)
        remaining = (100.0 - progress)/100.0*upgrade.FILE_SZ/speed
        self.ui.lb_progress.setText("速度(Byte/s)："+str(speed)+'\n'+"剩余时间："+time.strftime("%H时%M分%S秒", time.gmtime(remaining))+'\n'+"消耗时间："+time.strftime("%H时%M分%S秒", time.gmtime(time.time()- upgrade.START_TIME)))

    def upgrade_err_info(self, err):
        print(sys._getframe().f_code.co_name)
        match err:
            case 0:
                QtWidgets.QMessageBox.information(self,"提示", '升级成功')

            case -1:
                QtWidgets.QMessageBox.critical(self,"错误", 'MCU回复失败')

            case -2:
                QtWidgets.QMessageBox.critical(self,"错误", '升级包发送失败')

            case -3:
                QtWidgets.QMessageBox.critical(self,"错误", '重试失败')
        update_loop.terminate()


    # 中止升级
    def update_term(self):
        print(sys._getframe().f_code.co_name)
        update_loop.terminate()

    # 开始升级
    def startUpgrade(self):
        print(sys._getframe().f_code.co_name)
        update_loop.signal.connect(self.upgrade_progress)
        update_loop.err_signal.connect(self.upgrade_err_info)
        update_loop.start()
        upgrade.START_TIME = time.time()

    # 接收线程
    def recv_data_loop(self, recv_data2):
        global update_event, update_queue_start_cb, update_queue_send_cb
        if recv_data2.uID == 0x702:
            # print("0x702")
            test.SN1 = ""
            for i in recv_data2.arryData:
                # print("0x%02x" % i, end='\t')
                test.SN1 += "%02x" % i

        elif recv_data2.uID == 0x703:
            self.setWindowTitle("测试进行中。。。")
            # print("0x703")
            test.SN2 = ""
            for i in recv_data2.arryData:
                # print("0x%02x" % i, end='\t')
                test.SN2 += "%02x" % i
            self.ui.lb_sn.setText(test.SN1 + test.SN2)
            # print(test.SN)

        elif recv_data2.uID == 0x704:
            # print("0x704")
            test.STATE_MN = recv_data2.arryData[0]&0xF0 >> 4
            test.STATE_CPUN= recv_data2.arryData[0]&0x0F
            test.STATE_VMN= recv_data2.arryData[1]&0xF0 >> 4
            test.STATE_PN = recv_data2.arryData[1]&0x0F
            test.VERSION = recv_data2.arryData[2]

            self.ui.lb_state.setText("M卡数量："+str(test.STATE_MN)+'\t'+"CPU卡数量："+str(test.STATE_CPUN)+'\t'+"虚拟卡数量："+str(test.STATE_VMN)+'\t'+"唤醒引脚："+str(test.STATE_PN)+'\t'+"软件版本："+str(test.VERSION))
            # print(test.STATE_MN, test.STATE_CPUN, test.STATE_VMN, test.STATE_PN)

        elif recv_data2.uID == 0x705:
            print("0x705", end="\t")
            number = recv_data2.arryData[0]
            index = test.check_card_list(test.cpu_list, number)
            # print(index)
            if index < 0:
                # print("新序号")
                test.cpu_list.append(test.CPU_Card(number))
                # 获取索引
                index = test.check_card_list(test.cpu_list, number)

            test.cpu_list[index].uuid1 = ""
            length = recv_data2.arryData[1]
            for i in range(0, length):
                test.cpu_list[index].uuid1 += chr(recv_data2.arryData[i+2])
            # print(test.cpu_list[index].uuid1)


        elif recv_data2.uID == 0x706:
            print("0x706")

        elif recv_data2.uID == 0x707:
            print("0x707")

        elif recv_data2.uID == 0x708:
            print("0x708")

        elif recv_data2.uID == 0x709:
            print("0x709")

        elif recv_data2.uID == 0x70A:
            print("0x70A")

        elif recv_data2.uID == 0x70B:
            print("0x70B")

        elif recv_data2.uID == 0x70C:
            print("0x70C")

        elif recv_data2.uID == 0x70D:
            print("0x70D")

        elif recv_data2.uID == 0x70E:
            print("0x70E")

        elif recv_data2.uID == 0x70F:
            print("0x70F")

        elif recv_data2.uID == 0x710:
            print("0x710")

        elif recv_data2.uID == 0x711:
            print("0x711")

        elif recv_data2.uID == 0x712:
            print("0x712")

        elif recv_data2.uID == 0x713:
            print("0x713")

        elif recv_data2.uID == 0x714:
            print("0x714")

        elif recv_data2.uID == 0x715:
            print("0x715")

        elif recv_data2.uID == 0x716:
            print("0x716")


        elif recv_data2.uID == 0x731:
            print("0x731")
            update_queue_start_cb.put(recv_data2.arryData)

        elif recv_data2.uID == 0x733:
            # print("0x733")
            update_queue_send_cb.put(recv_data2.arryData)

        elif recv_data2.uID == 0x760:
            # print("0x760")
            length = recv_data2.arryData[0]
            UID = ""
            for i in range(0, length):
                UID += "%02x" % (recv_data2.arryData[i+1])
            test.CARD_CNT += 1
            self.ui.lb_cardcnt.setText("刷卡累计：%d"%test.CARD_CNT)
            QtWidgets.QMessageBox.information(self,"刷卡反馈", UID)

        elif recv_data2.uID == 0x3AE:
            # print("0x3AE")
            self.setWindowTitle("测试工具")



    # 初始化开启界面
    def init_data(self):
        for i in range(len(dwBtr_table['500Kbps'])):
            init_config.dwBtr[i] = dwBtr_table['500Kbps'][i]
            print('0x%x' % init_config.dwBtr[i], type(
                init_config.dwBtr[i]), end='\t')

        print("-->\t500Kbps")
        self.ui.pushButton_devClose.setEnabled(False)

    # 设备开启回调，启动接收线程
    def cb_dev_open(self):
        print("================================")
        # self.worker = recv_worker()
        recv_loop.signal.connect(self.recv_data_loop)
        recv_loop.start()

    # 开关测试模式
    def test_mode(self, mode, mode2):
        send_data = CAN_DataFrame(
            nSendType=0, bRemoteFlag=0, bExternFlag=0, nDataLen=8, uID=0x700)
        send_data.arryData[0] = mode
        send_data.arryData[1] = mode2
        res = pDll.CAN_ChannelSend(devHandle, 0, pointer(send_data), 1)
        if res != CAN_RESULT_ERROR:
            print("成功")
        else:
            print("失败")
            get_error_code(devHandle)

    # 打开测试模式
    def test_start(self):
        print("Start")
        test_mode_loop.start()
        self.test_mode(1,0)

    # 关闭测试模式
    def test_end(self):
        print("End")
        test_mode_loop.terminate()
        self.test_mode(0,0)

    # 选择USB端口
    def select_dev_comm(self, dwIndex):
        print("dwIndex: ", dwIndex, type(dwIndex), end='\t')
        global devCOM
        devCOM = dwIndex_table[dwIndex]
        print("devCOM: ", dwIndex_table[dwIndex])

    # 选择波特率
    def modify_dwBtr(self, bandRate):
        print("modify_dwBtr: ", bandRate, type(bandRate))
        for i in range(len(dwBtr_table[bandRate])):
            init_config.dwBtr[i] = dwBtr_table[bandRate][i]
            print('0x%x' % init_config.dwBtr[i], type(init_config.dwBtr[i]))

    # 打开设备
    def devOpen(self):
        print("打开设备:", USBCAN_1CH, end='\t')
        global devHandle, devCOM
        devHandle = pDll.CAN_DeviceOpen(USBCAN_1CH, devCOM)
        if devHandle != CAN_RESULT_ERROR:
            print("句柄:", devHandle, " USB", devCOM+1)
        else:
            print("失败")

        if self.ui.cb_res.checkState() == QtCore.Qt.Checked:
            print("检测到终端电阻 --> 开启")
            # pDll.CAN_WriteRegister(devHandle,0,0xfe,0)
            # pDll.CAN_WriteRegister(devHandle,0,0xfe,0x1)
            # pDll.CAN_WriteRegister(devHandle,0,0xff,0x1)
        elif self.ui.cb_res.checkState() == QtCore.Qt.Unchecked:
            print("检测到终端电阻 --> 关闭")
            # pDll.CAN_WriteRegister(devHandle,0,0xfe,0x1)
            # pDll.CAN_WriteRegister(devHandle,0,0xff,0x0)

        print("开启通道:", end='\t')
        res = pDll.CAN_ChannelStart(devHandle, 0, pointer(init_config))
        for i in range(len(init_config.dwBtr)):
            print('0x%02x' % init_config.dwBtr[i], type(
                init_config.dwBtr[i]), end='\t')
        if res != CAN_RESULT_ERROR:
            print("成功")
            self.cb_dev_open()
            self.ui.pushButton_devOpen.setEnabled(False)
            self.ui.pushButton_devClose.setEnabled(True)
        else:
            print("失败")

    # 关闭设备
    def devClose(self):
        print("关闭通道:", end='\t')
        global devHandle
        res = pDll.CAN_ChannelStop(devHandle, 0)
        if res != CAN_RESULT_ERROR:
            print("成功")
        else:
            print("失败")
        print("关闭设备:", devHandle, end='\t')
        res = pDll.CAN_DeviceClose(devHandle)
        if res != CAN_RESULT_ERROR:
            print("成功")
            recv_loop.terminate()
            self.ui.pushButton_devOpen.setEnabled(True)
            self.ui.pushButton_devClose.setEnabled(False)
        else:
            print("失败")

    def set_dev_res(self):
        print("终端电阻", end='\t')
        if self.ui.cb_res.checkState() == QtCore.Qt.Checked:
            print("开启")
        #     pDll.CAN_WriteRegister(devHandle,0,0xfe,0x1)
        #     pDll.CAN_WriteRegister(devHandle,0,0xff,0x1)
        elif self.ui.cb_res.checkState() == QtCore.Qt.Unchecked:
            print("关闭")
        #     pDll.CAN_WriteRegister(devHandle,0,0xfe,0x1)
        #     pDll.CAN_WriteRegister(devHandle,0,0xff,0x0)


    # 发送测试（没有用）
    def test_sendData(self):
        print("你点击了test_sendData")
        print("发送数据:", end='\t')
        send_data = CAN_DataFrame(
            nSendType=0, bRemoteFlag=0, bExternFlag=0, nDataLen=8, uID=0x1800070E)
        res = pDll.CAN_ChannelSend(devHandle, 0, pointer(send_data), 1)
        if res != CAN_RESULT_ERROR:
            print("成功")
        else:
            print("失败")
            get_error_code(devHandle)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    recv_loop = recv_worker()
    update_loop = update_worker()
    test_mode_loop = test_mode_keepalive()
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec())

