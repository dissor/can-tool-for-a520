from . CanCmd import *
from . can_recv_loop import *
from . can_keepalive_loop import *
from mainpre import *


class CANFunctions(MainWindow):
    # 打开设备
    def open(self):
        print("打开设备:", USBCAN_1CH, end='\t')

        # 获得端口
        dwIndex = self.ui.cb_set_usb.currentText()
        print("dwIndex: ", dwIndex, type(dwIndex), end='\t')
        can_dev.COM = dwIndex_table[dwIndex]

        # 打开设备
        can_dev.HANDLE = can_dev.PDLL.CAN_DeviceOpen(USBCAN_1CH, can_dev.COM)
        if can_dev.HANDLE != CAN_RESULT_ERROR:
            print("句柄:", can_dev.HANDLE, " USB", can_dev.COM+1)
        else:
            print("连接失败")
            return

        # 获得波特率
        bandRate = self.ui.cb_set_bps.currentText()
        print("波特率: ", bandRate, type(bandRate), end='\t')
        for i in range(len(dwBtr_table[bandRate])):
            can_dev.INIT.dwBtr[i] = dwBtr_table[bandRate][i]

        # 终端电阻
        # mask = 0x01 << 0
        # ctl = 0x01 << 0
        # can_dev.PDLL.CAN_WriteRegister(can_dev.HANDLE, 0, 0xfe, pointer(mask), 1)
        # can_dev.PDLL.CAN_WriteRegister(can_dev.HANDLE, 0, 0xff, pointer(ctl), 1)

        print("开启通道: 0", end='\t')
        res = can_dev.PDLL.CAN_ChannelStart(
            can_dev.HANDLE, 0, pointer(can_dev.INIT))
        if res != CAN_RESULT_ERROR:
            print("成功")
        else:
            print("失败")
            return

        # 开启接收线程和保活线程
        recv_task.start()
        alive_task.start()

        self.ui.lb_credits.setText(
            Settings.CREDIT + '\t' + Settings.HEARTBEAT+"开\t" + Settings.CONNECT+"成功")
        self.ui.btn_set_open.setEnabled(False)
        self.ui.btn_set_close.setEnabled(True)

    # 关闭设备
    def close(self):

        # 关闭接收线程和保活线程
        recv_task.terminate()
        alive_task.terminate()

        print("关闭通道: 0", end='\t')
        res = can_dev.PDLL.CAN_ChannelStop(can_dev.HANDLE, 0)
        if res != CAN_RESULT_ERROR:
            print("成功", end='\t')
        else:
            print("失败")
            return
        print("关闭句柄:", can_dev.HANDLE, end='\t')
        res = can_dev.PDLL.CAN_DeviceClose(can_dev.HANDLE)
        if res != CAN_RESULT_ERROR:
            print("成功")
        else:
            print("失败")
            return

        self.ui.lb_credits.setText(
            Settings.CREDIT + '\t' + Settings.HEARTBEAT+"关\t" + Settings.CONNECT+"断开")
        self.ui.btn_set_open.setEnabled(True)
        self.ui.btn_set_close.setEnabled(False)

    # def get_error_code(can_dev.HANDLE):
    #     print("获取错误信息:")
    #     err_info = CAN_ErrorInformation()
    #     p_err_info = pointer(err_info)
    #     res = can_dev.can_dev.PDLL.CAN_GetErrorInfo(
    #         can_dev.HANDLE, 0, p_err_info)
    #     if res != CAN_RESULT_ERROR:
    #         print(err_info.uErrorCode)
    #         print(err_info.PassiveErrData)
    #         print(err_info.ArLostErrData)
    #     else:
    #         print("失败")
