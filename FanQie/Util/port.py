from Util.dos_cmd import DosCmd


class Port:
    def __init__(self):
        self.dos = DosCmd()

    def port_is_used(self, port_num):
        """
        判断端口是否被占用
        :param port_num: 端口号
        :return: Boolean
        """
        command = 'lsof -i tcp:' + str(port_num)
        result = self.dos.excute_cmd_result(command)
        if len(result) > 0:
            flag = True
        else:
            flag = False
        return flag

    def create_port_list(self, start_port, device_list):
        """
        生成可用端口
        :param start_port: 开始端口
        :param device_list: 设备列表
        :return: list
        """
        port_list = []
        if device_list is not None:
            while len(port_list) != len(device_list):
                if self.port_is_used(start_port) is not True:
                    port_list.append(start_port)
                start_port += 1
            return port_list
        else:
            print('设备列表为空,请检查设备连接是否完好')
            return None


if __name__ == '__main__':
    port = Port()
    print(port.port_is_used('4724'))
