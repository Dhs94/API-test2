# coding:utf-8
import smtplib
from email.mime.text import MIMEText
import yagmail


class SendMail:

    def send_mail(self, receiver_list, sub, content):
        host = "smtp.qq.com"
        sender = "282410983@qq.com"
        password = "ryprfozwyqawbgfg"
        # user = "admin"+"<"+sender+">"
        # 邮件内容
        # message = MIMEText(content, _subtype='plain', _charset='utf-8')
        # message['Subject'] = sub
        # message['From'] = sender
        # message['To'] = ";".join(receiver_list)
        # server = smtplib.SMTP()
        # # 连接服服务器
        # server.connect(host=host)
        # # 登录
        # server.login(user=sender, password=password)
        # server.sendmail(from_addr=user, to_addrs=receiver_list, msg=message.as_string())
        # server.close()
        yag = yagmail.SMTP(user=sender, password=password, host=host)
        yag.send(to=receiver_list, subject=sub, contents=content)

    def send_main(self, pass_list, fail_list):
        pass_count = float(len(pass_list))
        fail_count = float(len(fail_list))
        run_count = pass_count + fail_count
        # %.2f取两位小数，%%取百分值
        pass_result = "%.2f%%" % (pass_count / run_count * 100)
        fail_result = "%.2f%%" % (fail_count / run_count * 100)
        sub = "WDMS接口测试邮件"
        content = "本次测试结果如下：\n执行用例总数：%d\n通过数：%d\n失败数：%d\n通过率：%s\n失败率：%s\n" % (
                run_count, pass_count, fail_count, pass_result, fail_result)
        receiver = "282410983@qq.com"
        self.send_mail(receiver, sub, content)


if __name__ == '__main__':
    send = SendMail()
    pl1 = [1, 2]
    pl2 = [3, 4]
    send.send_main(pl1, pl2)
