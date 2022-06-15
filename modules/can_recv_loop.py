from mainpre import *
from . CanCmd import *

class can_recv_worker(QThread):

    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            # 阻塞接收
            res = can_dev.PDLL.CAN_ChannelReceive(
                can_dev.HANDLE, 0, pointer(can_dev.RECV), 1, 0xFFFF)
            # print("get date", res, len)
            if res != CAN_RESULT_ERROR:
                self.cb_can_receive(can_dev.RECV)
                print("接收正确")
            else:
                can_dev.PDLL.CAN_ClearReceiveBuffer(can_dev.HANDLE, 0)
                print("接收错误")

    def cb_can_receive(self, data):
        print(data.uID)
        for i in range(data.nDataLen):
            print(data.arryData[i], end='\t')
        print("接收完成")

recv_task = can_recv_worker()
