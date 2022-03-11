FILE_NAME = ""
FILE_FD = ""
FILE_SZ = ""
FILE_CNT = ""
CRC16 = 0
START_TIME = 0.0

def crc16(addr, len):
    crc = 0
    key = 0xE32A

    if len > 0:
        for i in range(len):
            crc ^= addr[i]
            for j in range(8):
                if crc & 1 != 0:
                    crc = (crc >> 1)^key
                else:
                    crc = (crc >> 1)
    return crc
