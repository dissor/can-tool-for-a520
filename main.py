import sys
import time
import os
import crc16
from NJLikeLib.CanCmd import *
from PySide6 import QtWidgets, QtCore
from threading import Thread, Event
from queue import Queue
from UI import ui_00login, ui_01test, ui_02upgrade, ui_03write
from DB import test, upgrade

# 升级同步事件
update_event = Event()
update_queue_start_cb = Queue()
update_queue_send_cb = Queue()

# 接收线程类
class recv_worker(QtCore.QThread):
    def __init__(self):
        super().__init__()

    def run(self):
        global recv_data
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
        widget.recv_data_loop(recv_data1)

# 升级线程类
class update_worker(QtCore.QThread):
    def __init__(self):
        super().__init__()

    def run(self):
        global update_event, update_queue_start_cb, update_queue_send_cb
        print(sys._getframe().f_code.co_name)
        global devHandle
        bytes = 6

        # '//'表示向下取整除法
        upgrade.FILE_CNT = upgrade.FILE_SZ//bytes

        if upgrade.FILE_SZ % bytes > 0:
            upgrade.FILE_CNT += 1

        # 都是int型
        # print(type(upgrade.FILE_SZ), type(upgrade.FILE_CNT))

        psend_data = CAN_DataFrame(nSendType=0, bRemoteFlag=0,
                                   bExternFlag=0, nDataLen=8, uID= 0x730)

        # 固件大小
        for i in range(0, 4):
            psend_data.arryData[i] = (upgrade.FILE_SZ >> (8*i)) & 0xFF

        # 总包数
        for i in range(0, 2):
            psend_data.arryData[i+4] = (upgrade.FILE_CNT >> (8*i)) & 0xFF

        # CRC16校验

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
                print(upgrade.FILE_FD.read(bytes))

        else:
            print("禁止升级")

        psend_data.uID= 0x732

        for index in range(0, upgrade.FILE_CNT):
            upgrade.FILE_FD.seek(bytes*index)
            print(index, bytes*index, end='\t')
            # for i in upgrade.FILE_FD.read(bytes):
            #     print(hex(i), end='\t')

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

            res = pDll.CAN_ChannelSend(devHandle, 0, pointer(psend_data), 1)
            if res != CAN_RESULT_ERROR:
                # print("升级包发送成功")

                # 等待设备回复
                data_res = update_queue_send_cb.get()
                if data_res[0] == 0:
                    print("接收成功: ",index/upgrade.FILE_CNT*100)
                    widget.ui.progressBar.setValue(index/upgrade.FILE_CNT*100)
                else:
                    print("接收失败")
                    for i in data_res:
                        print(hex(i), end='\t')
            else:
                print("升级包发送失败")



class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.ui = ui_00login.Ui_Form()  # 实例化UI对象
        self.ui.setupUi(self)  # 初始化

        self.init_data()

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
        print(upgrade.FILE_SZ)
        self.ui.lb_binsize.setText("%d" % upgrade.FILE_SZ+" bytes")

        # 使用open函数打开文件，打开模式选择二进制读取'rb'
        upgrade.FILE_FD = open(upgrade.FILE_NAME, 'rb')

        # upgrade.FILE_FD.seek(0)
        # print(upgrade.FILE_FD.read(4))
        # for i in upgrade.FILE_FD:
        #     print(i)
        # upgrade.FILE_FD.close()

    # 开始升级
    def startUpgrade(self):
        # update_loop.start()
        global update_event, update_queue_start_cb, update_queue_send_cb
        print(sys._getframe().f_code.co_name)
        global devHandle
        bytes = 6

        # '//'表示向下取整除法
        upgrade.FILE_CNT = upgrade.FILE_SZ//bytes

        if upgrade.FILE_SZ % bytes > 0:
            upgrade.FILE_CNT += 1

        # 都是int型
        # print(type(upgrade.FILE_SZ), type(upgrade.FILE_CNT))

        psend_data = CAN_DataFrame(nSendType=0, bRemoteFlag=0,
                                   bExternFlag=0, nDataLen=8, uID= 0x730)

        # 固件大小
        for i in range(0, 4):
            psend_data.arryData[i] = (upgrade.FILE_SZ >> (8*i)) & 0xFF

        # 总包数
        for i in range(0, 2):
            psend_data.arryData[i+4] = (upgrade.FILE_CNT >> (8*i)) & 0xFF

        # CRC16校验

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
                print(upgrade.FILE_FD.read(bytes))

        else:
            print("禁止升级")

        psend_data.uID= 0x732

        for index in range(0, upgrade.FILE_CNT):
            upgrade.FILE_FD.seek(bytes*index)
            print(index, bytes*index, end='\t')
            # for i in upgrade.FILE_FD.read(bytes):
            #     print(hex(i), end='\t')

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

            res = pDll.CAN_ChannelSend(devHandle, 0, pointer(psend_data), 1)
            if res != CAN_RESULT_ERROR:
                # print("升级包发送成功")

                # 等待设备回复
                data_res = update_queue_send_cb.get(timeout = 5)
                if data_res[0] == 0:
                    print("接收成功: ",index/upgrade.FILE_CNT*100)
                    self.ui.progressBar.setValue(index/upgrade.FILE_CNT*100)
                else:
                    print("接收失败")
                    for i in data_res:
                        print(hex(i), end='\t')
                    break
            else:
                print("升级包发送失败")
                break

        print("升级结束")


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

            self.ui.lb_state.setText("M卡数量："+str(test.STATE_MN)+'\t'+"CPU卡数量："+str(test.STATE_CPUN)+'\t'+"虚拟卡数量："+str(test.STATE_VMN)+'\t'+"唤醒引脚："+str(test.STATE_PN))
            # print(test.STATE_MN, test.STATE_CPUN, test.STATE_VMN, test.STATE_PN)

        elif recv_data2.uID == 0x705:
            print("0x705")

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
        recv_loop.start()

    # 开关测试模式
    def test_mode(self, mode):
        send_data = CAN_DataFrame(
            nSendType=0, bRemoteFlag=0, bExternFlag=0, nDataLen=8, uID=0x700)
        send_data.arryData[0] = mode
        res = pDll.CAN_ChannelSend(devHandle, 0, pointer(send_data), 1)
        if res != CAN_RESULT_ERROR:
            print("成功")
        else:
            print("失败")
            get_error_code(devHandle)

    # 打开测试模式
    def test_start(self):
        print("Start")
        self.test_mode(1)

    # 关闭测试模式
    def test_end(self):
        print("End")
        self.test_mode(0)

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
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec())
