from mainpre import *

# 接口卡类型定义
USBCAN_1CH = 13

# 函数调用返回状态值
CAN_RESULT_OK = 1
CAN_RESULT_ERROR = 0

# CAN数据帧类型
class CAN_DataFrame(Structure):
    _fields_ = [
        ("uTimeFlag",   c_uint),    # 时间标识,对接收帧有效
        ("nSendType",   c_ubyte),   # 发送帧类型,0-正常发送;1-单次发送;2-自发自收;3-单次自发自收
        ("bRemoteFlag", c_ubyte),   # 是否是远程帧
        ("bExternFlag", c_ubyte),   # 是否是扩展帧
        ("nDataLen",    c_ubyte),   # 数据长度
        ("uID",         c_uint),    # 报文DI
        ("arryData",    c_ubyte*8)  # 报文数据
    ]

# CAN初始化配置
class CAN_InitConfig(Structure):
    _fields_ = [
        ("bMode",      c_ubyte),    # 工作模式(0表示正常模式,1表示只听模式)
        ("nBtrType",   c_ubyte),    # 位定时参数模式(1表示SJA1000,0表示LPC21XX)
        ("dwBtr",      c_ubyte*4),  # CAN位定时参数
        ("dwAccCode",  c_ulong),    # 验收码
        ("dwAccMask",  c_ulong),    # 屏蔽码
        ("nFilter",    c_ubyte),    # 滤波方式(0表示未设置滤波功能,1表示双滤波,2表示单滤波)
        ("dwReserved", c_ubyte)     # 预留字段
    ]

# CAN设备信息
class CAN_DeviceInformation(Structure):
    _fields_ = [
        ("uHardWareVersion",  c_ushort),   # 硬件版本
        ("uFirmWareVersion",  c_ushort),   # 固件版本
        ("uDriverVersion",    c_ushort),   # 驱动版本
        ("uInterfaceVersion", c_ushort),   # 接口库版本
        ("uInterruptNumber",  c_ushort),   # 有几路CAN
        ("bChannelNumber",    c_ubyte),    # 报文DI
        ("szSerialNumber",    c_char*20),  # 设备序列号
        ("szHardWareType",    c_char*40),  # 硬件类型
        ("szDescription",     c_char*20)   # 设备描述
    ]

# CAN错误信息
class CAN_ErrorInformation(Structure):
    _fields_ = [
        ("uErrorCode",     c_uint),     # 错误类型
        ("PassiveErrData", c_ubyte*3),  # 消极错误数据
        ("ArLostErrData",  c_ubyte)     # 仲裁错误数据
    ]

# 端口哈希
dwIndex_table = {
    'USB1': 0,
    'USB2': 1,
    'USB3': 2,
    'USB4': 3,
    'USB5': 4,
    'USB6': 5,
    'USB7': 6,
    'USB8': 7,
    'USB9': 8,
    'USB10': 9,
    'USB11': 10,
    'USB12': 11,
    'USB13': 12,
    'USB14': 13,
    'USB15': 14,
    'USB16': 15,
}

# 波特率哈希
dwBtr_table = {
    '5Kbps': [0xBF, 0xFF],
    '10Kbps': [0x31, 0x1C],
    '20Kbps': [0x18, 0x1C],
    '50Kbps': [0x09, 0x1C],
    '100Kbps': [0x04, 0x1C],
    '125Kbps': [0x03, 0x1C],
    '250Kbps': [0x01, 0x1C],
    '500Kbps': [0x00, 0x1C],
    '800Kbps': [0x00, 0x16],
    '1000Kbps': [0x00, 0x14],
}

# 加载动态库
pDll = CDLL("./NJLikeLib/CanCmd.dll")

devHandle = 0  # device handle
devInfo = CAN_DeviceInformation()
devCOM = 0  # device comm
init_config = CAN_InitConfig(bMode=0, nBtrType=1)
err_info = CAN_ErrorInformation()
send_data = CAN_DataFrame(nSendType=0, bRemoteFlag=0,
                          bExternFlag=0, nDataLen=8)
recv_data = CAN_DataFrame()

def get_error_code(devHandle):
    print("获取错误信息:")
    err_info = CAN_ErrorInformation()
    p_err_info = pointer(err_info)
    res = pDll.CAN_GetErrorInfo(devHandle, 0, p_err_info)
    if res != CAN_RESULT_ERROR:
        print(err_info.uErrorCode)
        print(err_info.PassiveErrData)
        print(err_info.ArLostErrData)
    else:
        print("失败")
