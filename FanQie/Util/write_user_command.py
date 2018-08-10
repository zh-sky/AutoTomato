import yaml


class WriteUserCommand:
    def __init__(self):
        self.file_path = '../Config/userConfig.yaml'

    def read_data(self):
        """
        加载yaml数据
        :return:
        """
        with open(self.file_path) as fr:
            data = yaml.load(fr)
        print(data)
        return data

    def get_value(self, key, port):
        """
        从 yaml 中获取数据  根据key port 找到对应的value
        :param key:
        :param port:
        :return: value
        """
        data = self.read_data()
        value = data[key][port]
        return value

    def write_data(self, i, device, bp, port):
        """
        向yaml文件中写入数据
        :return:
        """
        data = self.join_data(i, device, bp, port)
        with open(self.file_path, 'a') as fr:
            yaml.dump(data, fr)

    def join_data(self, i, device, bp, port):
        """
        拼接数据
        :param i: 第几行
        :param device: 设备名称
        :param bp: bootstrap号
        :param port: 端口号
        :return: 字典
        """
        data = {
            'user_info_'+str(i): {
                'deviceName': device,
                'bp': bp,
                'port': port
            }
        }
        return data

    def clear_data(self):
        """
        写入数据之前需进行清空数据的操作  防止重复
        :return:
        """
        with open(self.file_path, 'w') as fr:
            fr.truncate()
        fr.close()

    def get_lines(self):
        """
        获取yaml文件中数据的行数
        :return:
        """
        data = self.read_data()
        return len(data)

