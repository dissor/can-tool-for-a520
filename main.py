from NJLikeLib.CanCmd import *


# 1.打开设备
# 调用动态链接库函数
print("打开设备:", USBCAN_1CH)
devHandle = pDll.CAN_DeviceOpen(USBCAN_1CH, 0)
# 打印返回结果
if devHandle != CAN_RESULT_ERROR:
    print("句柄：", devHandle)
else:
    print("失败")



# 2.获取设备信息
print("获取设备信息:")
devInfo = CAN_DeviceInformation()

res = pDll.CAN_GetDeviceInfo(devHandle, pointer(devInfo))
print(devInfo.szDescription)
if res != CAN_RESULT_ERROR:
    print("成功")
else:
    print("失败")
    get_error_code(devHandle)


# 3.开启通道
print("开启通道:")
init_config = CAN_InitConfig(bMode=0, nBtrType=1)
init_config.dwBtr[0] = 0x01   # 250 Kbps
init_config.dwBtr[1] = 0x1c

res = pDll.CAN_ChannelStart(devHandle, 0, pointer(init_config))
if res != CAN_RESULT_ERROR:
    print("成功")
else:
    print("失败")
    get_error_code()


# # 4.获取错误信息
# print("获取错误信息:")
# err_info = CAN_ErrorInformation()
# p_err_info = pointer(err_info)
# res = pDll.CAN_GetErrorInfo(devHandle, 0, p_err_info)
# if res != CAN_RESULT_ERROR:
#     print("成功")
# else:
#     print("失败")


# 5.发送/接收通道数据
print("发送数据:")
send_data = CAN_DataFrame(nSendType=0,bRemoteFlag=0,bExternFlag=0,nDataLen=8,uID=0x1800070E)

res = pDll.CAN_ChannelSend(devHandle, 0, pointer(send_data), 1)
if res != CAN_RESULT_ERROR:
    print("成功")
else:
    print("失败")
    get_error_code(devHandle)



# 6.获取接收计数/清空接收缓冲


# 7.关闭通道
print("关闭通道:")
res = pDll.CAN_ChannelStop(devHandle, 0)
if res != CAN_RESULT_ERROR:
    print("成功")
else:
    print("失败")


# 8.关闭设备
print("关闭设备:")
res = pDll.CAN_DeviceClose(devHandle)
if res != CAN_RESULT_ERROR:
    print("成功")
else:
    print("失败")


