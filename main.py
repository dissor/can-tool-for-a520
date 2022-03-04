import sys
import time
import os
import crc16
from NJLikeLib.CanCmd import *
from PySide6 import QtWidgets, QtCore
from threading import Thread, Event
from UI import ui_00login, ui_01test, ui_02upgrade, ui_03write
from DB import test, upgrade

# 升级同步事件
update_event = Event()


class test_class():
    def sn(self):
        print("sn")

    def state(self):
        print("state")

    def uuid(self):
        print("uuid")

    def okey(self):
        print("okey")

    def usrkey(self):
        print("usrkey")

    def usrdata(self):
        print("usrdata")

    def mkeya(self):
        print("mkeya")

    def mkeyb(self):
        print("mkeyb")

    def musrdata(self):
        print("musrdata")

    def muuid(self):
        print("muuid")

    def vmuuid(self):
        print("vmuuid")


class recv_worker(QtCore.QThread):
    def __init__(self):
        super().__init__()

    def run(self):
        global recv_data
        while True:
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
            else:
                time.sleep(1)

    def cb_can_receive(self, recv_data1):
        # print("cb_can_receive:0x%x" % recv_data1.uID,
        #       "len: ", len(recv_data1.arryData))
        widget.recv_data_loop()


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.ui = ui_00login.Ui_Form()  # 实例化UI对象
        self.ui.setupUi(self)  # 初始化

        self.init_data()

    def ceshi_api(self):
        print(sys._getframe().f_code.co_name)
        # self.ui.lb_sn.setText(recv_data.arryData[0])

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

    def startUpgrade(self):
        print(sys._getframe().f_code.co_name)

        # '//'表示向下取整除法
        upgrade.FILE_CNT = upgrade.FILE_SZ//6

        if upgrade.FILE_SZ % 6 > 0:
            upgrade.FILE_CNT += 1

        # 都是int型
        print(type(upgrade.FILE_SZ), type(upgrade.FILE_CNT))

        psend_data = CAN_DataFrame(nSendType=0, bRemoteFlag=0,
                                   bExternFlag=0, nDataLen=8)

        # 固件大小
        for i in range(0, 4):
            psend_data.arryData[i] = (upgrade.FILE_SZ >> (8*i)) & 0xFF

        # 总包数
        for i in range(0, 2):
            psend_data.arryData[i+4] = (upgrade.FILE_CNT >> (8*i)) & 0xFF

        # CRC16校验

        for i in range(0, 8):
            print( hex(psend_data.arryData[i]), end='\t')

        res = pDll.CAN_ChannelSend(devHandle, 0, pointer(send_data), 1)
        if res != CAN_RESULT_ERROR:
            print("成功")
        else:
            print("失败")

    def recv_data_loop(self):
        global update_event
        if recv_data.uID == 0x702:
            print("0x702")
            test.SN = ""
            for i in recv_data.arryData:
                # print("0x%02x" % i, end='\t')
                test.SN += "%02x" % i

        elif recv_data.uID == 0x703:
            print("0x703")
            for i in recv_data.arryData:
                # print("0x%02x" % i, end='\t')
                test.SN += "%02x" % i
            self.ui.lb_sn.setText(test.SN)
            print(test.SN)
            test.SN = ""

        elif recv_data.uID == 0x731:
            print("0x731")

        elif recv_data.uID == 0x733:
            print("0x733")

    def init_data(self):
        for i in range(len(dwBtr_table['500Kbps'])):
            init_config.dwBtr[i] = dwBtr_table['500Kbps'][i]
            print('0x%x' % init_config.dwBtr[i], type(
                init_config.dwBtr[i]), end='\t')

        print("-->\t500Kbps")

    def cb_dev_open(self):
        print("================================")
        self.worker = recv_worker()
        self.worker.start()

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

    def test_start(self):
        print("Start")
        self.test_mode(1)

    def test_end(self):
        print("End")
        self.test_mode(0)

    def select_dev_comm(self, dwIndex):
        print("dwIndex: ", dwIndex, type(dwIndex), end='\t')
        global devCOM
        devCOM = dwIndex_table[dwIndex]
        print("devCOM: ", dwIndex_table[dwIndex])

    def modify_dwBtr(self, bandRate):
        print("modify_dwBtr: ", bandRate, type(bandRate))
        for i in range(len(dwBtr_table[bandRate])):
            init_config.dwBtr[i] = dwBtr_table[bandRate][i]
            print('0x%x' % init_config.dwBtr[i], type(init_config.dwBtr[i]))

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
        else:
            print("失败")

    def devClose(self):
        print("关闭通道:", end='\t')
        res = pDll.CAN_ChannelStop(devHandle, 0)
        if res != CAN_RESULT_ERROR:
            print("成功")
        else:
            print("失败")
        print("关闭设备:", devHandle, end='\t')
        res = pDll.CAN_DeviceClose(devHandle)
        if res != CAN_RESULT_ERROR:
            print("成功")
        else:
            print("失败")

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
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec())
