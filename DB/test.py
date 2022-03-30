
SN1, SN2 = "", ""
STATE_MN, STATE_CPUN, STATE_VMN, STATE_PN = "", "", "", ""
UUID1, UUID2 = "", ""
CARD_CNT = 0
OKEY = ""
USRKEY = ""
USRDATA = ""
MKEYA = ""
MKEYB = ""
MUSRDATA = ""
MUUID = ""
VMUUID = ""
VERSION = 0

# CPU卡
class CPU_Card(object):
    def __init__(self, number = None):
        self.number = number
        self.uuid1 = "uuid1"
        self.uuid2 = "uuid2"
        self.out_key1 = "out_key1"
        self.out_key2 = "out_key2"
        self.user_key1 = "user_key1"
        self.user_key2 = "user_key2"
        self.user_data1 = "user_data1"
        self.user_data2 = "user_data2"

cpu_list = []

# M1卡
class M1_Card(object):
    def __init__(self, number = ""):
        self.number = number
        self.uuid = "uuid"
        self.key_a = "key_a"
        self.key_b = "key_b"
        self.user_data = "user_data"

m1_list = []

# 模拟卡
class VM_Card(object):
    def __init__(self, number = ""):
        self.number = number
        self.uuid = "uuid"

vm_list = []

def check_card_list(mlist = [], number = ""):
    for i in mlist:
        if i.number == number:
            return mlist.index(i)
    return -1

