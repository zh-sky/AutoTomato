import configparser


class ReadIni:
    def __init__(self, file_path=None):
        if file_path is None:
            self.file_path = '/Users/mike/AutoTomato/FanQie/Config/fanqieElement.ini'
        else:
            self.file_path = file_path

    def get_value(self, section, key):
        read_ini = configparser.ConfigParser()
        read_ini.read(self.file_path, encoding='utf-8')
        try:
            value = read_ini.get(section, key)
        except:
            value = None
        return value


if __name__ == '__main__':
    read = ReadIni()
    print(read.get_value('login_element', 'username'))
