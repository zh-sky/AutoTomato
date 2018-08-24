from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.header import Header
from email.utils import parseaddr, formataddr
from email import encoders
import os
import time
import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def send_file(file_name):
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    subject = '番茄来了自动化测试报告'+now
    user = '15721525908@163.com'
    passWord = 'huanhuan163'
    server = 'smtp.163.com'
    receiver = ['18310226539@163.com', '1903203367@qq.com', 'huanhuan.zhang@fangbaba.com']

    content = MIMEText('测试报告', 'plain', 'utf-8')

    with open(file_name, 'r', encoding='utf-8') as file:
        # content_type = 'application/octet-stream'
        # main_type, subtype = content_type.split('/', 1)
        #
        # # 读入文件内容并格式化
        # accessory = MIMEBase(file.read(), 'html', filename='番茄来了自动化测试报告')
        #
        # # 加上必要的头信息
        # accessory.add_header('Content-Disposition', 'attachment', filename='番茄来了自动化测试报告')
        # accessory.add_header('Content-ID', '<0>')
        # accessory.add_header('X-Attachment-Id', '0')
        # # 读入文件内容并格式化 用base64编码
        # accessory.set_payload(file.read())
        # encoders.encode_base64(accessory)

        file = file.read()
        accessory = MIMEText(file, 'html', 'utf-8')

        # 附件设置内容类型 方便起见，设置为二进制流
        accessory.add_header('Content-Type', 'application/octet-stream')
        # 设置附件头， 添加文件名
        accessory.add_header('Content-Disposition', 'attachment', filename=('gb2312', '', '番茄来了自动化测试报告'))

    # 设置根容器属性
    msg_root = MIMEMultipart()
    msg_root['subject'] = subject
    msg_root['From'] = _format_addr('测试组<%s>' % user)
    msg_root['To'] = _format_addr('番茄来了项目组 <%s>' % ';'.join(receiver))
    msg_root.attach(content)
    msg_root.attach(accessory)

    try:
        smtp = smtplib.SMTP_SSL(server, '465')
        smtp.login(user, passWord)
        # msg_root.as_string() 得到格式化后的完整文本
        smtp.sendmail(user, receiver, msg_root.as_string())
        smtp.quit()
    except smtplib.SMTPException as e:
        print(e)


# 查找指定文件目录 获取最新生成的测试报告
def new_report(test_report):
    lists = os.listdir(test_report)
    lists.sort(key=lambda fn: os.path.getmtime(test_report + '/' +fn))
    file_new = os.path.join(test_report, lists[-1])
    print(file_new)
    return file_new


if __name__ == '__main__':
    report = new_report('/Users/mike/AutoTomato/FanQie/report')
    send_file(report)
