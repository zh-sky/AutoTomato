# coding:utf-8
import os



class DosCmd:

    def excute_cmd_result(self, command):
        result_list = []
        result = os.popen(command).readlines().decode('utf-8')
        # print(result)
        for udid in result:
            print(udid)
            result_list.append(udid.strip('\n'))
        return result_list

    def excute_cmd(self, command):
        os.system(command)


if __name__ == '__main__':
    dos = DosCmd()
    print(dos.excute_cmd_result('ideviceinstaller -l'))
