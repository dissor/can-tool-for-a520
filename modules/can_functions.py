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

    def buttonClick(self, btnName):

        # 正常发送，数据帧，标准帧，8字节长度，id700
        send_data = CAN_DataFrame(
            nSendType=0, bRemoteFlag=0, bExternFlag=0, nDataLen=8, uID=0x700)

        if btnName == "btn_test_start":
            send_data.arryData[0] = 1
            send_data.arryData[1] = 0



        if btnName == "btn_test_stop":
            send_data.arryData[0] = 0
            send_data.arryData[1] = 0


        res = can_dev.PDLL.CAN_ChannelSend(can_dev.HANDLE, 0, pointer(send_data), 1)
        if res != CAN_RESULT_ERROR:
            print("成功")
        else:
            print("失败")
            self.get_error_code()

    def get_error_code(self):
        print("获取错误信息:")
        err_info = CAN_ErrorInformation()
        p_err_info = pointer(err_info)
        res = can_dev.PDLL.CAN_GetErrorInfo(
            can_dev.HANDLE, 0, p_err_info)
        if res != CAN_RESULT_ERROR:
            print(err_info.uErrorCode)
            print(err_info.PassiveErrData)
            print(err_info.ArLostErrData)
        else:
            print("失败")

    def openUpdateFile(self):
        print(sys._getframe().f_code.co_name)
        fd_name = ""
        # 参数 _ 用于分割第二个返回值，防止 fd 生成数组
        fd_path, _ = QFileDialog.getOpenFileName(
            self, "选择文件", "", "BIN(*.bin);;All Files(*)")
        self.ui.le_update_edit.setText(fd_path)

        fd_size = os.path.getsize(fd_path)
        print("升级包大小：" + str(fd_size), end="\t")
        item01 = QTableWidgetItem()
        item01.setText("%d" % fd_size)
        self.ui.tw_update_item.setItem(0, 1, item01)

        # 使用open函数打开文件，打开模式选择二进制读取'rb'
        fd = open(fd_path, 'rb')

        # CRC16校验
        crc16, key = 0, 0xE32A
        # print(type(crc16))
        for i in fd.read():
            # print(hex(i), end=",")
            crc16 ^= i
            for j in range(8):
                if crc16 & 1 != 0:
                    crc16 = (crc16 >> 1) ^ key
                else:
                    crc16 = (crc16 >> 1)

        print("crc16: ", crc16, hex(crc16), end='\t')

        # 补齐 CRC
        date_bytes = 6
        re_len = fd_size % date_bytes
        if re_len != 0:
            print("最后一包长度：", re_len)
            for i in range(date_bytes - re_len):
                crc16 ^= 0xFF
                for j in range(8):
                    if crc16 & 1 != 0:
                        crc16 = (crc16 >> 1) ^ key
                    else:
                        crc16 = (crc16 >> 1)
        print("修正crc16: ", crc16, hex(crc16))
