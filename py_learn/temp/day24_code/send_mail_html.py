# 发送html内容的邮件

# 所用发送方邮箱的授权码
# 163邮箱:CXFVAMFQXMABDHRB

# 导入模块
import smtplib  # 发送邮件
from email.mime.text import MIMEText    # email：构建邮件    MIMEText：文本对象
from email.mime.multipart import MIMEMultipart      # 构建多个内容

# 需求：使用163邮箱给qq邮箱及其他邮箱发送邮件
def send_data():
    # 1.准备工作
    # smtp服务器地址
    mail_host = 'smtp.163.com'
    # 发送方的邮箱账号
    mail_sender = 'jiangliang_c@163.com'
    # 发送方的授权码，注意：不是邮箱的登录密码，而是开启smtp协议时获取到的授权码
    mail_pwd = 'CXFVAMFQXMABDHRB'

    # 2.构建邮件内容
    # 正文内容
    data = MIMEMultipart()
    # 主题/标题
    data['Subject'] = '2023年7月7日发送html邮件测试'
    # 发送方
    data['From'] = mail_sender
    # 接受方
    receviers = ['599397252@qq.com','loveuqiaoxin@gmail.com']
    data['To'] = ';'.join(receviers)
    html_str = '''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <h1>邮件正文部分</h1>
    <table width="500" border="1" cellspacing="0">
        <tr>
            <td>张三</td>
            <td>10</td>
            <td>male</td>
            <td>唱歌</td>
        </tr>
        <tr>
            <td>李四</td>
            <td>34</td>
            <td>male</td>
            <td>打碟</td>
        </tr>
        <tr>
            <td>王五</td>
            <td>23</td>
            <td>male</td>
            <td>吃饭</td>
        </tr>
    </table>
    <ul>
        <li>人事部</li>
        <li>财务部</li>
        <li>市场部</li>
        <li>研发部</li>
    </ul>
</body>
</html>
    '''
    data.attach(MIMEText(html_str,'html','utf-8'))

    # 3.发送邮件
    # 连接对象 = smtplib.SMTP_SSL(服务器地址,邮箱服务端口)
    smtp_connector = smtplib.SMTP_SSL(mail_host, 465)
    # 进行登录
    # 连接对象.login(发送方，授权码)
    smtp_connector.login(mail_sender,mail_pwd)
    # 发送： 连接对象.sendmail(发件人，收件人，邮件对象.as_string())
    smtp_connector.sendmail(mail_sender,receviers,data.as_string())
    smtp_connector.quit()

if __name__ == '__main__':
   send_data()
