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