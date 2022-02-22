import sys
from NJLikeLib.CanCmd import *
from PySide6 import QtWidgets
from UI.ui_main import *


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        for i in range(len(dwBtr_table['5Kbps'])):
            init_config.dwBtr[i] = dwBtr_table['5Kbps'][i]
            print('0x%x' % init_config.dwBtr[i], type(init_config.dwBtr[i]))

        ui = Ui_Form()  # 实例化UI对象
        ui.setupUi(self)  # 初始化

    def modify_dwBtr(self, bandRate):
        print("modify_dwBtr: ", bandRate, type(bandRate))
        for i in range(len(dwBtr_table[bandRate])):
            init_config.dwBtr[i] = dwBtr_table[bandRate][i]
            print('0x%x' % init_config.dwBtr[i], type(init_config.dwBtr[i]))

    def devOpen(self):
        print("打开设备:", USBCAN_1CH, end='\t')
        global devHandle
        devHandle = pDll.CAN_DeviceOpen(USBCAN_1CH, 0)
        if devHandle != CAN_RESULT_ERROR:
            print("句柄:", devHandle)
        else:
            print("失败")

        print("开启通道:", end='\t')
        res = pDll.CAN_ChannelStart(devHandle, 0, pointer(init_config))
        for i in range(len(init_config.dwBtr)):
            print('0x%02x' % init_config.dwBtr[i], type(init_config.dwBtr[i]))
        if res != CAN_RESULT_ERROR:
            print("成功")
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
