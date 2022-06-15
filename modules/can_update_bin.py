
# 升级线程类
class update_worker(QtCore.QThread):
    signal = QtCore.Signal(float)
    err_signal = QtCore.Signal(int)

    def __init__(self):
        super().__init__()

    def run(self):
        global update_event, update_queue_start_cb, update_queue_send_cb, devHandle
        bytes = 6

        # '//'表示向下取整除法
        upgrade.FILE_CNT = upgrade.FILE_SZ//bytes

        if upgrade.FILE_SZ % bytes > 0:
            upgrade.FILE_CNT += 1

        # 都是int型
        # print(type(upgrade.FILE_SZ), type(upgrade.FILE_CNT))
        print("升级包大小：%d" % upgrade.FILE_SZ+"\t升级总包数：%d" % upgrade.FILE_CNT)

        psend_data = CAN_DataFrame(nSendType=0, bRemoteFlag=0,
                                   bExternFlag=0, nDataLen=8, uID=0x730)

        # 固件大小
        for i in range(0, 4):
            psend_data.arryData[i] = (upgrade.FILE_SZ >> (8*i)) & 0xFF

        # 总包数
        for i in range(0, 2):
            psend_data.arryData[i+4] = (upgrade.FILE_CNT >> (8*i)) & 0xFF

        # CRC16校验
        for i in range(0, 2):
            psend_data.arryData[i+6] = (upgrade.CRC16 >> (8*i)) & 0xFF

        # 打印报文
        # for i in range(0, 8):
        #     print( hex(psend_data.arryData[i]), end='\t')

        res = pDll.CAN_ChannelSend(devHandle, 0, pointer(psend_data), 1)
        if res != CAN_RESULT_ERROR:
            print("成功")
        else:
            print("失败")

        data_res = update_queue_start_cb.get()
        # for i in data_res:
        #     print(hex(i))

        if data_res[0] == 0:
            print("允许升级")
            for i in range(0, upgrade.FILE_CNT):
                upgrade.FILE_FD.seek(bytes*upgrade.FILE_CNT)
                # print(upgrade.FILE_FD.read(bytes))

        else:
            print("禁止升级")

        psend_data.uID = 0x732

        for index in range(upgrade.FILE_CNT):
            upgrade.FILE_FD.seek(bytes*index)
            print(hex(index), hex(bytes*index), end='\t')
            # for i in upgrade.FILE_FD.read(bytes):
            #     print(hex(i), end='\t')

            # 初始化
            for i in range(8):
                psend_data.arryData[i] = 0xFF

            # 包索引
            for i in range(0, 2):
                psend_data.arryData[i] = (index >> (8*i)) & 0xFF

            # 数据
            tmp = 2
            for i in upgrade.FILE_FD.read(bytes):
                psend_data.arryData[tmp] = i
                tmp += 1
                # print(hex(upgrade.FILE_FD.read(bytes)[i]), end='\t')

            # for i in psend_data.arryData:
            #     print(hex(i), end='\t')

            # 重试8次
            for i in range(0, 8):
                res = pDll.CAN_ChannelSend(
                    devHandle, 0, pointer(psend_data), 1)
                if res != CAN_RESULT_ERROR:
                    # print("升级包发送成功")

                    # 等待设备回复
                    try:
                        data_res = update_queue_send_cb.get(timeout=10)
                    except Exception as err:
                        print("异常：%s" % err+"重试次数：%d" % i)
                        continue

                    progress = index/upgrade.FILE_CNT*100
                    if data_res[0] == 0:
                        print("回复成功：", progress)
                        self.signal.emit(progress)
                        if index == upgrade.FILE_CNT-1:
                            self.signal.emit(100)
                            self.err_signal.emit(0)
                            return
                        break
                    else:
                        print("回复失败：")
                        for i in data_res:
                            print(hex(i), end='\t')
                        self.err_signal.emit(-1)
                        # todo: 是否考虑重试3次
                        break
                else:
                    print("升级包发送失败")
                    self.err_signal.emit(-2)
                    break

        f'重试8次依旧失败'
        self.err_signal.emit(-3)