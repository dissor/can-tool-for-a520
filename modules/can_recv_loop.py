from mainpre import *
from . CanCmd import *

class can_recv_worker(QThread):
    # signal = Signal(type(CAN_DEV.RECV))

    def __init__(self):
        super().__init__()
        # self.signal.connect(self.upgrade_progress)

    def run(self):
        while True:
            # 阻塞接收
            res = CAN_DEV.PDLL.CAN_ChannelReceive(
                CAN_DEV.HANDLE, 0, pointer(CAN_DEV.RECV), 1, 0xFFFFFFFF)
            # print("get date", res, len)
            if res != CAN_RESULT_ERROR:
                self.cb_can_receive(CAN_DEV.RECV)
            else:
                CAN_DEV.PDLL.CAN_ClearReceiveBuffer(CAN_DEV.HANDLE, 0)
                print("接收错误")

    def cb_can_receive(self, data):
        print(data)
        # self.signal.emit(CAN_DEV.RECV1)

recv_task = can_recv_worker()
