from mainpre import *
from . CanCmd import *
import time

class test_mode_keepalive(QThread):
    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            psend_data = CAN_DataFrame(nSendType=0, bRemoteFlag=0,
                                       bExternFlag=0, nDataLen=8, uID=0x750)

            for i in range(0, 8):
                psend_data.arryData[i] = 0x00

            if can_dev.PDLL.CAN_ChannelSend(can_dev.HANDLE, 0, pointer(psend_data), 1) == CAN_RESULT_ERROR:
                print("心跳发送失败")

            time.sleep(1)

alive_task = test_mode_keepalive()