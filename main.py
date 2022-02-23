import sys, time
from NJLikeLib.CanCmd import *
from PySide6 import QtWidgets, QtCore
from UI import ui_00login,ui_01test, ui_02upgrade, ui_03write

class recv_worker(QtCore.QThread):
    def __init__(self):
        super().__init__()

    def run(self):
        global recv_data
        while True:
            len = pDll.CAN_GetReceiveCount(devHandle, 0)
            print("get date len", len)
            if len > 0:
                res = pDll.CAN_ChannelReceive(devHandle, 0, pointer(recv_data), 1, -1)
                print("get date res", res)
                if res != CAN_RESULT_ERROR:
                    print("0x%x"%recv_data.uID, end='\t')
                    for i in range(0, 8):
                        # print('0x%x' % init_config.dwBtr[i], type(init_config.dwBtr[i]), end='\t')
                        print("0x%02x"%recv_data.arryData[i], end='\t')
                else:
                    print("recv worker is running")
            else:
                time.sleep(1)

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.ui = ui_00login.Ui_Form()  # 实例化UI对象
        self.ui.setupUi(self)  # 初始化

        self.init_data()

    def init_data(self):
        for i in range(len(dwBtr_table['500Kbps'])):
            init_config.dwBtr[i] = dwBtr_table['500Kbps'][i]
            print('0x%x' % init_config.dwBtr[i], type(init_config.dwBtr[i]), end='\t')

        print("-->\t500Kbps")

    def cb_dev_open(self):
        print("================================")
        self.worker = recv_worker()
        self.worker.start()


    def test_start(self):
        print("Start")
        send_data = CAN_DataFrame(
            nSendType=0, bRemoteFlag=0, bExternFlag=0, nDataLen=8, uID=0x700)
        res = pDll.CAN_ChannelSend(devHandle, 0, pointer(send_data), 1)
        if res != CAN_RESULT_ERROR:
            print("成功")
        else:
            print("失败")
            get_error_code(devHandle)

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
        global devHandle,devCOM
        devHandle = pDll.CAN_DeviceOpen(USBCAN_1CH, devCOM)
        if devHandle != CAN_RESULT_ERROR:
            print("句柄:", devHandle, " USB", devCOM+1)
        else:
            print("失败")

        print("开启通道:", end='\t')
        res = pDll.CAN_ChannelStart(devHandle, 0, pointer(init_config))
        for i in range(len(init_config.dwBtr)):
            print('0x%02x' % init_config.dwBtr[i], type(init_config.dwBtr[i]), end='\t')
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
