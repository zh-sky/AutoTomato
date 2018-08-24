from Util.dos_cmd import DosCmd
from Util.port import Port
from Util.write_user_command import WriteUserCommand
import threading
import time
import Util.common


class Server:
    def __init__(self):
        self.dos = DosCmd()
        self.device_list = self.dos.excute_cmd_result(Util.common.find_device)
        self.write_file = WriteUserCommand()
        self.start_list = self.create_command_list()

    def create_port_list(self, start_port):
        """
        创建可用端口
        :return: list
        """
        port = Port()
        port_list = port.create_port_list(start_port, self.device_list)
        return port_list

    def create_command_list(self):
        """
        生成dos命令  # appium -p 4700 -bp 4701 -U deviceName
        :return: list
        """
        command_list = []
        appium_port_list = self.create_port_list(4723)
        bootstrap_port_list = self.create_port_list(4900)
        for i in range(len(self.device_list)):
            command = 'appium -p '+str(appium_port_list[i])+' -bp '+str(bootstrap_port_list[i])+' -U '+self.device_list[i]+' --no-reset --session-override'
            command_list.append(command)
            # 向 yaml 文件中写入数据
            self.write_file.write_data(i, str(self.device_list[i]), str(bootstrap_port_list[i]), str(appium_port_list[i]))

        return command_list

    def start_server(self, i):
        """
        根据命令开启服务
        :return: None
        """
        self.dos.excute_cmd(self.start_list[i])

    def main(self):
        # self.write_file.clear_data()
        for i in range(len(self.start_list)):
            appium_start = threading.Thread(target=self.start_server, args=(i,))
            appium_start.start()
        # 命令行启动需要一定的是时间，所以休眠一段时间以保证后续操作可以正常执行
        time.sleep(10)


if __name__ == '__main__':
    server = Server()
    server.main()
