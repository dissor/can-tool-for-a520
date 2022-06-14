from . CanCmd import *
from mainpre import *

    # # 选择USB端口
    # def select_dev_comm(self, dwIndex):
    #     print("dwIndex: ", dwIndex, type(dwIndex), end='\t')
    #     global devCOM
    #     devCOM = dwIndex_table[dwIndex]
    #     print("devCOM: ", dwIndex_table[dwIndex])

    # # 选择波特率
    # def modify_dwBtr(self, bandRate):
    #     print("modify_dwBtr: ", bandRate, type(bandRate))
    #     for i in range(len(dwBtr_table[bandRate])):
    #         init_config.dwBtr[i] = dwBtr_table[bandRate][i]
    #         print('0x%x' % init_config.dwBtr[i], type(init_config.dwBtr[i]))

class CANFunctions(MainWindow):

    # 打开设备
    def open(self):
        print("打开设备:", USBCAN_1CH, end='\t')

        # 获得端口
        dwIndex = self.ui.cb_set_usb.currentText()
        print("dwIndex: ", dwIndex, type(dwIndex), end='\t')
        CAN_DEV.COM = dwIndex_table[dwIndex]

        # 打开设备
        CAN_DEV.HANDLE = CAN_DEV.PDLL.CAN_DeviceOpen(USBCAN_1CH, CAN_DEV.COM)
        if CAN_DEV.HANDLE != CAN_RESULT_ERROR:
            print("句柄:", CAN_DEV.HANDLE, " USB", CAN_DEV.COM+1)
        else:
            print("连接失败")
            return

        # 获得波特率
        bandRate = self.ui.cb_set_bps.currentText()
        print("波特率: ", bandRate, type(bandRate), end='\t')
        for i in range(len(dwBtr_table[bandRate])):
            CAN_DEV.INIT.dwBtr[i] = dwBtr_table[bandRate][i]

        # 终端电阻
        # mask = 0x01 << 0
        # ctl = 0x01 << 0
        # CAN_DEV.PDLL.CAN_WriteRegister(CAN_DEV.HANDLE, 0, 0xfe, pointer(mask), 1)
        # CAN_DEV.PDLL.CAN_WriteRegister(CAN_DEV.HANDLE, 0, 0xff, pointer(ctl), 1)

        print("开启通道: 0", end='\t')
        res = CAN_DEV.PDLL.CAN_ChannelStart(CAN_DEV.HANDLE, 0, pointer(CAN_DEV.INIT))
        if res != CAN_RESULT_ERROR:
            print("成功")
        else:
            print("失败")
            return

        self.ui.btn_set_open.setEnabled(False)
        self.ui.btn_set_close.setEnabled(True)

    # 关闭设备
    def close(self):
        print("关闭通道: 0", end='\t')
        res = CAN_DEV.PDLL.CAN_ChannelStop(CAN_DEV.HANDLE, 0)
        if res != CAN_RESULT_ERROR:
            print("成功", end='\t')
        else:
            print("失败")
            return
        print("关闭句柄:", CAN_DEV.HANDLE, end='\t')
        res = CAN_DEV.PDLL.CAN_DeviceClose(CAN_DEV.HANDLE)
        if res != CAN_RESULT_ERROR:
            print("成功")
        else:
            print("失败")
            return

        self.ui.btn_set_open.setEnabled(True)
        self.ui.btn_set_close.setEnabled(False)

    # def get_error_code(CAN_DEV.HANDLE):
    #     print("获取错误信息:")
    #     err_info = CAN_ErrorInformation()
    #     p_err_info = pointer(err_info)
    #     res = CAN_DEV.CAN_DEV.PDLL.CAN_GetErrorInfo(
    #         CAN_DEV.HANDLE, 0, p_err_info)
    #     if res != CAN_RESULT_ERROR:
    #         print(err_info.uErrorCode)
    #         print(err_info.PassiveErrData)
    #         print(err_info.ArLostErrData)
    #     else:
    #         print("失败")
