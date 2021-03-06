import sys
import time
import os
# import crc16
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
                                       bExternFlag=0, nDataLen=8, uID=0x750)

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
        print("升级包大小：%d" % upgrade.FILE_SZ+"\t升级总包数：%d" % upgrade.FILE_CNT)

        psend_data = CAN_DataFrame(nSendType=0, bRemoteFlag=0,
                                   bExternFlag=0, nDataLen=8, uID=0x730)

        # 固件大小
        for i in range(0, 4):
            psend_data.arryData[i] = (upgrade.FILE_SZ >> (8*i)) & 0xFF

        # 总包数
        for i in range(0, 2):
            psend_data.arryData[i+4] = (upgrade.FILE_CNT >> (8*i)) & 0xFF

        # CRC16校验
        for i in range(0, 2):
            psend_data.arryData[i+6] = (upgrade.CRC16 >> (8*i)) & 0xFF

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

        psend_data.uID = 0x732

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
                res = pDll.CAN_ChannelSend(
                    devHandle, 0, pointer(psend_data), 1)
                if res != CAN_RESULT_ERROR:
                    # print("升级包发送成功")

                    # 等待设备回复
                    try:
                        data_res = update_queue_send_cb.get(timeout=10)
                    except Exception as err:
                        print("异常：%s" % err+"重试次数：%d" % i)
                        continue

                    progress = index/upgrade.FILE_CNT*100
                    if data_res[0] == 0:
                        print("回复成功：", progress)
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
            self.test_mode(1, 1)
        if res_text == "模拟卡":
            print("模拟卡")
            self.test_mode(1, 2)
        if res_text == "解绑卡":
            print("解绑卡")
            self.test_mode(1, 3)

    def peika_stop(self):
        print(sys._getframe().f_code.co_name)
        res_text = self.ui.comboBox.currentText()
        if res_text == "实体卡":
            print("实体卡")
            self.test_mode(0, 1)
        if res_text == "模拟卡":
            print("模拟卡")
            self.test_mode(0, 2)

    # 写SN号
    def writeNumber(self):
        print(sys._getframe().f_code.co_name)
        m_str = self.ui.lineEdit.text()

        msend_data = CAN_DataFrame(
            nSendType=0, bRemoteFlag=0, bExternFlag=0, nDataLen=8)
        msend_data.uID = 0x740

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
                    upgrade.CRC16 = (upgrade.CRC16 >> 1) ^ key
                else:
                    upgrade.CRC16 = (upgrade.CRC16 >> 1)

        print("upgrade.CRC16: ", upgrade.CRC16, hex(upgrade.CRC16), end='\t')

        # 补齐 CRC
        re_len = upgrade.FILE_SZ % upgrade.BYTES
        if re_len != 0:
            print("最后一包长度：", re_len)
            for i in range(upgrade.BYTES - re_len):
                upgrade.CRC16 ^= 0xFF
                for j in range(8):
                    if upgrade.CRC16 & 1 != 0:
                        upgrade.CRC16 = (upgrade.CRC16 >> 1) ^ key
                    else:
                        upgrade.CRC16 = (upgrade.CRC16 >> 1)
        print("修正upgrade.CRC16: ", upgrade.CRC16, hex(upgrade.CRC16))

    def upgrade_progress(self, progress):
        # print(sys._getframe().f_code.co_name)
        self.ui.progressBar.setValue(progress)
        speed = progress/100.0*upgrade.FILE_SZ / \
            (time.time() - upgrade.START_TIME)
        remaining = (100.0 - progress)/100.0*upgrade.FILE_SZ/speed
        self.ui.lb_progress.setText("速度(Byte/s)："+str(speed)+'\n'+"剩余时间："+time.strftime("%H时%M分%S秒", time.gmtime(
            remaining))+'\n'+"消耗时间："+time.strftime("%H时%M分%S秒", time.gmtime(time.time() - upgrade.START_TIME)))

    def upgrade_err_info(self, err):
        print(sys._getframe().f_code.co_name)
        # match err:
        if err == 0:
            QtWidgets.QMessageBox.information(self, "提示", '升级成功')

        if err == -1:
            QtWidgets.QMessageBox.critical(self, "错误", 'MCU回复失败')

        if err == -2:
            QtWidgets.QMessageBox.critical(self, "错误", '升级包发送失败')

        if err == -3:
            QtWidgets.QMessageBox.critical(self, "错误", '重试失败')
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
            test.STATE_MN = recv_data2.arryData[0] & 0xF0 >> 4
            test.STATE_CPUN = recv_data2.arryData[0] & 0x0F
            test.STATE_VMN = recv_data2.arryData[1] & 0xF0 >> 4
            test.STATE_PN = recv_data2.arryData[1] & 0x0F
            test.VERSION = recv_data2.arryData[2]

            self.ui.lb_shui.setText("水位：%d"%recv_data2.arryData[3])

            self.ui.lb_state.setText("M卡数量："+str(test.STATE_MN)+'\t'+"CPU卡数量："+str(test.STATE_CPUN)+'\t'+"虚拟卡数量："+str(
                test.STATE_VMN)+'\t'+"唤醒引脚："+str(test.STATE_PN)+'\t'+"软件版本："+str(test.VERSION))
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

        elif recv_data2.uID == 0x718:
            print("0x718")
            self.ui.lb_temp.setText("温度：%d"%recv_data2.arryData[0])

        elif recv_data2.uID == 0x731:
            print("0x731")
            update_queue_start_cb.put(recv_data2.arryData)

        elif recv_data2.uID == 0x733:
            # print("0x733")
            update_queue_send_cb.put(recv_data2.arryData)

        elif recv_data2.uID == 0x760:
            # print("0x760")
            length = recv_data2.arryData[0] % 0x10
            flag = (recv_data2.arryData[0] & 0b00010000) >> 4
            UID = ""
            for i in range(0, length):
                UID += "%02x" % (recv_data2.arryData[i+1])
            test.CARD_CNT += 1
            self.ui.lb_cardcnt.setText("刷卡累计：%d" % test.CARD_CNT)
            # if flag == 1:
            #     QtWidgets.QMessageBox.information(self, "刷卡(已配对)", UID)
            # else:
            #     QtWidgets.QMessageBox.information(self, "刷卡(未配对)", UID)

        elif recv_data2.uID == 0x3AE:
            # print("0x3AE")
            self.setWindowTitle("测试工具")

        elif recv_data2.uID == 0x65:
            data_len = recv_data2.nDataLen

            # 显示所有UID
            if recv_data2.arryData[0] == 0xF8:
                global uuidQueue
                for i in range(3, data_len - 1):
                    uuidQueue.put(recv_data2.arryData[i])

                if recv_data2.arryData[2] == 0:
                    uidLen = uuidQueue.qsize()
                    uidStr = ""
                    for i in range(uidLen):
                        if i%8 == 0 and i != 0:
                            uidStr += '\r\n'
                        elif i != 0:
                            uidStr += ' - '
                        hexd = uuidQueue.get()
                        if hexd <= 0xf:
                            uidStr += '0'
                        uidStr += hex(hexd)[2:]

                    self.ui.textBrowser.setText(uidStr)

            #FIXME: 显示密钥
            if recv_data2.arryData[0] == 0xF5:
                global pakeyQue
                for i in range(3, data_len - 1):
                    pakeyQue.put(recv_data2.arryData[i])

                if recv_data2.arryData[2] == 0:
                    uidLen = pakeyQue.qsize()
                    if uidLen == 32*2:
                        self.ui.cb_p16.setChecked(False)
                        self.ui.cb_a16.setChecked(False)
                    else:
                        self.ui.cb_p16.setChecked(True)
                        self.ui.cb_a16.setChecked(True)
                    self.select_picc_16()
                    self.select_app_16()
                    piccStr = ""
                    for i in range(int(uidLen/2)):
                        hexd = pakeyQue.get()
                        if hexd <= 0xf:
                            piccStr += '0'
                        piccStr += hex(hexd)[2:]

                    self.ui.lineEdit_2.setText(piccStr)

                    appStr = ""
                    for i in range(int(uidLen/2)):
                        hexd = pakeyQue.get()
                        if hexd <= 0xf:
                            appStr += '0'
                        appStr += hex(hexd)[2:]

                    self.ui.lineEdit_3.setText(appStr)

            #FIXME: 显示ic密钥
            if recv_data2.arryData[0] == 0xFB:
                global icpakeyQue
                for i in range(3, data_len - 1):
                    icpakeyQue.put(recv_data2.arryData[i])

                if recv_data2.arryData[2] == 0:
                    uidLen = icpakeyQue.qsize()
                    if uidLen == 32*2:
                        self.ui.cb_k16.setChecked(False)
                    else:
                        self.ui.cb_k16.setChecked(True)
                    self.select_ic_16()
                    icStr = ""
                    for i in range(uidLen):
                        hexd = icpakeyQue.get()
                        if hexd <= 0xf:
                            icStr += '0'
                        icStr += hex(hexd)[2:]

                    self.ui.lineEdit_4.setText(icStr)


    # 初始化开启界面

    def init_data(self):
        for i in range(len(dwBtr_table['500Kbps'])):
            init_config.dwBtr[i] = dwBtr_table['500Kbps'][i]
            print('0x%x' % init_config.dwBtr[i], type(
                init_config.dwBtr[i]), end='\t')

        # 初始化密钥限制16进制
        str1, str2 = "", ""
        for i in range(16):
            str1 += 'HH '
        for i in range(15):
            str2 += 'HH '
        str2 += 'HH;#'

        if(self.ui.cb_p16.isChecked()):
            self.ui.lineEdit_2.setInputMask(str2)
        else:
            self.ui.lineEdit_2.setInputMask(str1 + str2)

        if(self.ui.cb_a16.isChecked()):
            self.ui.lineEdit_3.setInputMask(str2)
        else:
            self.ui.lineEdit_3.setInputMask(str1 + str2)

        if(self.ui.cb_k16.isChecked()):
            self.ui.lineEdit_4.setInputMask(str2)
        else:
            self.ui.lineEdit_4.setInputMask(str1 + str2)

        self.ui.lineEdit_5.setInputMask('HH HH HH HH HH HH HH HH;#')
        self.ui.lineEdit_6.setInputMask('HH HH HH HH HH HH HH HH;#')

        # self.ui.lineEdit_2.setInputMask(
        #     'HH HH HH HH HH HH HH HH HH HH HH HH HH HH HH HH;#')
        # self.ui.lineEdit_3.setInputMask(
        #     'HH HH HH HH HH HH HH HH HH HH HH HH HH HH HH HH;#')
        # self.ui.lineEdit_4.setInputMask(
        #     'HH HH HH HH HH HH HH HH HH HH HH HH HH HH HH HH HH HH HH HH HH HH HH HH HH HH HH HH HH HH HH HH;#')
        # print("-->\t500Kbps")
        self.ui.pushButton_devClose.setEnabled(False)

        # FIXME: This 初始化队列
        global uuidQueue
        uuidQueue = Queue(maxsize = 1024)
        global pakeyQue
        pakeyQue = Queue(maxsize = 1024)
        global icpakeyQue
        icpakeyQue = Queue(maxsize = 1024)


        # for i in range(64):
        #     pakeyQue.put(i)

        # s1 = ''
        # for i in range(32):
        #     hexd = pakeyQue.get()
        #     if hexd <= 0xf:
        #         s1 += '0'
        #     s1 += hex(hexd)[2:]

        # self.ui.lineEdit_2.setText(s1)



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
        self.test_mode(1, 0)

    # 关闭测试模式
    def test_end(self):
        print("End")
        test_mode_loop.terminate()
        self.test_mode(0, 0)

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

    # 写卡密钥
    def write_card_id(self):
        crc = 0
        send_data = CAN_DataFrame(
            nSendType=0, bRemoteFlag=0, bExternFlag=0, nDataLen=8, uID=0x65)

        m_str2 = self.ui.lineEdit_2.text()
        m_str3 = self.ui.lineEdit_3.text()

        if self.ui.cb_p16.isChecked():
            if len(m_str2) != 16*2 + 16 - 1:
                print("format error20:", len(m_str2))
                return
        else:
            if len(m_str2) != 32*2 + 32 - 1:
                print("format error21:", len(m_str2))
                return

        if self.ui.cb_a16.isChecked():
            if len(m_str3) != 16*2 + 16 - 1:
                print("format error30:", len(m_str3))
                return
        else:
            if len(m_str3) != 32*2 + 32 - 1:
                print("format error31:", len(m_str3))
                return

        key_str = m_str2.split(" ") + m_str3.split(" ")
        print(key_str, len(key_str))

        keyQue = Queue(maxsize= 1024)

        for i in range(len(key_str)):
            ai = int.from_bytes(bytes.fromhex(key_str[i]), byteorder='little')
            print(ai, type(ai))
            keyQue.put(ai)

        # PiccKey 5
        send_data.arryData[0] = 0xF1

        for i in range(int(len(key_str)/4)):
            send_data.arryData[1] = i
            send_data.arryData[2] = int(len(key_str)/4) - (i + 1)
            for ii in range(4):
                send_data.arryData[ii+3] = keyQue.get()
            send_data.arryData[7] = 0x00
            send_data.arryData[7] = self.uuidCrc(send_data.arryData)
            for j in range(8):
                print(send_data.arryData[j], end=' ')
            res = pDll.CAN_ChannelSend(devHandle, 0, pointer(send_data), 1)
            if res != CAN_RESULT_ERROR:
                print("成功")
            else:
                print("失败")
                get_error_code(devHandle)


    # 读卡密钥

    def read_card_id(self):
        send_data = CAN_DataFrame(
            nSendType=0, bRemoteFlag=0, bExternFlag=0, nDataLen=4, uID=0x60)

        send_data.arryData[0] = 0xFE
        send_data.arryData[1] = 0x04
        send_data.arryData[2] = 0xF3
        send_data.arryData[3] = self.uuidCrc(send_data.arryData)
        res = pDll.CAN_ChannelSend(devHandle, 0, pointer(send_data), 1)
        if res != CAN_RESULT_ERROR:
            print("成功")
        else:
            print("失败")
            get_error_code(devHandle)

    # TODO: 写IC密钥
    def write_ic_id(self):
        send_data = CAN_DataFrame(
            nSendType=0, bRemoteFlag=0, bExternFlag=0, nDataLen=8, uID=0x65)

        m_str4 = self.ui.lineEdit_4.text()

        if self.ui.cb_k16.isChecked():
            if len(m_str4) != 16*2 + 16 - 1:
                print("format error40:", len(m_str4))
                return
        else:
            if len(m_str4) != 32*2 + 32 - 1:
                print("format error41:", len(m_str4))
                return

        print(m_str4, len(m_str4))
        key_str = m_str4.split(" ")


        keyQue = Queue(maxsize= 1024)

        for i in range(len(key_str)):
            ai = int.from_bytes(bytes.fromhex(key_str[i]), byteorder='little')
            print(ai, type(ai))
            keyQue.put(ai)

        # PiccKey 5
        send_data.arryData[0] = 0xF2

        for i in range(int(len(key_str)/4)):
            send_data.arryData[1] = i
            send_data.arryData[2] = int(len(key_str)/4) - (i + 1)
            for ii in range(4):
                send_data.arryData[ii+3] = keyQue.get()
            send_data.arryData[7] = 0x00
            send_data.arryData[7] = self.uuidCrc(send_data.arryData)
            for j in range(8):
                print(send_data.arryData[j], end=' ')
            res = pDll.CAN_ChannelSend(devHandle, 0, pointer(send_data), 1)
            if res != CAN_RESULT_ERROR:
                print("成功")
            else:
                print("失败")
                get_error_code(devHandle)

    # 删除所有UID
    def delete_all_uid(self):
        print("删除所有UID")
        send_data = CAN_DataFrame(
            nSendType=0, bRemoteFlag=0, bExternFlag=0, nDataLen=4, uID=0x60)

        send_data.arryData[0] = 0xFE
        send_data.arryData[1] = 0x04
        send_data.arryData[2] = 0xF4
        send_data.arryData[3] = self.uuidCrc(send_data.arryData)

        res = pDll.CAN_ChannelSend(devHandle, 0, pointer(send_data), 1)
        if res != CAN_RESULT_ERROR:
            print("成功")
            self.ui.textBrowser.setText('')
        else:
            print("失败")
            get_error_code(devHandle)

    # 读取所有UID
    def read_all_uid(self):
        print("读取所有UID")
        send_data = CAN_DataFrame(
            nSendType=0, bRemoteFlag=0, bExternFlag=0, nDataLen=4, uID=0x60)

        send_data.arryData[0] = 0xFE
        send_data.arryData[1] = 0x04
        send_data.arryData[2] = 0xF7
        send_data.arryData[3] = self.uuidCrc(send_data.arryData)

        res = pDll.CAN_ChannelSend(devHandle, 0, pointer(send_data), 1)
        if res != CAN_RESULT_ERROR:
            print("成功")
        else:
            print("失败")
            get_error_code(devHandle)

    def uuidCrc(self, data):
        zeroD = 0
        for i in data:
            zeroD -= i
        return zeroD & 0xFF

    # TODO: implement
    def select_picc_16(self):
        status = self.ui.cb_p16.isChecked()
        print("select_picc_16", status)
        str1, str2 = "", ""
        for i in range(16):
            str1 += 'HH '
        for i in range(15):
            str2 += 'HH '
        str2 += 'HH;#'
        if(self.ui.cb_p16.isChecked()):
            self.ui.lineEdit_2.setInputMask(str2)
        else:
            self.ui.lineEdit_2.setInputMask(str1 + str2)

    def select_app_16(self):
        status = self.ui.cb_a16.isChecked()
        print("select_app_16", status)
        str1, str2 = "", ""
        for i in range(16):
            str1 += 'HH '
        for i in range(15):
            str2 += 'HH '
        str2 += 'HH;#'

        if(self.ui.cb_a16.isChecked()):
            self.ui.lineEdit_3.setInputMask(str2)
        else:
            self.ui.lineEdit_3.setInputMask(str1 + str2)

    def select_ic_16(self):
        status = self.ui.cb_k16.isChecked()
        print("select_ic_16", status)
        str1, str2 = "", ""
        for i in range(16):
            str1 += 'HH '
        for i in range(15):
            str2 += 'HH '
        str2 += 'HH;#'
        if(self.ui.cb_k16.isChecked()):
            self.ui.lineEdit_4.setInputMask(str2)
        else:
            self.ui.lineEdit_4.setInputMask(str1 + str2)

    #TODO: 写uid
    def write_uid_single(self):
        send_data = CAN_DataFrame(
            nSendType=0, bRemoteFlag=0, bExternFlag=0, nDataLen=8, uID=0x65)

        m_str5 = self.ui.lineEdit_5.text()

        if len(m_str5) != 8*2 + 8 - 1:
            print("format error51:", len(m_str5))
            return

        print(m_str5, len(m_str5))
        key_str = m_str5.split(" ")


        keyQue = Queue(maxsize= 1024)

        for i in range(len(key_str)):
            ai = int.from_bytes(bytes.fromhex(key_str[i]), byteorder='little')
            print(ai, type(ai))
            keyQue.put(ai)

        send_data.arryData[0] = 0xF6

        for i in range(int(len(key_str)/4)):
            send_data.arryData[1] = i
            send_data.arryData[2] = int(len(key_str)/4) - (i + 1)
            for ii in range(4):
                send_data.arryData[ii+3] = keyQue.get()
            send_data.arryData[7] = 0x00
            send_data.arryData[7] = self.uuidCrc(send_data.arryData)
            for j in range(8):
                print(send_data.arryData[j], end=' ')
            res = pDll.CAN_ChannelSend(devHandle, 0, pointer(send_data), 1)
            if res != CAN_RESULT_ERROR:
                print("成功")
            else:
                print("失败")
                get_error_code(devHandle)

    # TODO: 读取ic密钥
    def read_ic_key(self):
        print("读取IC密钥")
        send_data = CAN_DataFrame(
            nSendType=0, bRemoteFlag=0, bExternFlag=0, nDataLen=4, uID=0x60)

        send_data.arryData[0] = 0xFE
        send_data.arryData[1] = 0x04
        send_data.arryData[2] = 0xFA
        send_data.arryData[3] = self.uuidCrc(send_data.arryData)

        res = pDll.CAN_ChannelSend(devHandle, 0, pointer(send_data), 1)
        if res != CAN_RESULT_ERROR:
            print("成功")
        else:
            print("失败")
            get_error_code(devHandle)

    # FIXME: 删除指定UID
    def delect_uid_single(self):
        send_data = CAN_DataFrame(
            nSendType=0, bRemoteFlag=0, bExternFlag=0, nDataLen=8, uID=0x65)

        m_str6 = self.ui.lineEdit_6.text()

        if len(m_str6) != 8*2 + 8 - 1:
            print("format error61:", len(m_str6))
            return

        print(m_str6, len(m_str6))
        key_str = m_str6.split(" ")


        keyQue = Queue(maxsize= 1024)

        for i in range(len(key_str)):
            ai = int.from_bytes(bytes.fromhex(key_str[i]), byteorder='little')
            print(ai, type(ai))
            keyQue.put(ai)

        send_data.arryData[0] = 0xFC

        for i in range(int(len(key_str)/4)):
            send_data.arryData[1] = i
            send_data.arryData[2] = int(len(key_str)/4) - (i + 1)
            for ii in range(4):
                send_data.arryData[ii+3] = keyQue.get()
            send_data.arryData[7] = 0x00
            send_data.arryData[7] = self.uuidCrc(send_data.arryData)
            for j in range(8):
                print(send_data.arryData[j], end=' ')
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
