# 发送图片容的邮件

# 所用发送方邮箱的授权码
# 163邮箱:CXFVAMFQXMABDHRB

# 导入模块
import smtplib  # 发送邮件
from email.mime.text import MIMEText    # email：构建邮件    MIMEText：文本对象
from email.mime.multipart import MIMEMultipart      # 构建多个内容
from email.mime.image import MIMEImage      # 构建图片

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
    data['Subject'] = '2023年7月7日发送图片邮件测试'
    # 发送方
    data['From'] = mail_sender
    # 接受方
    receviers = ['599397252@qq.com','loveuqiaoxin@gmail.com']
    data['To'] = ';'.join(receviers)

    # 读取图片内容
    with open(r'data/img.png','rb') as f:
        img_data = f.read()
    # 方式一：构建图片对象【图片会被识别为福建】
    # img = MIMEImage(img_data)
    # data.attach(img)
    
    # 方式二
    img = MIMEImage(img_data)
    img.add_header('Content-ID','add_pic')  # add_pic 是用来在html中识别图片的id
    html_str = '''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
   <h2>这是一个带有图片的邮件</h2>
   <p>
       <img src="cid:add_pic">
   </p>
</body>
</html>
    '''
    data.attach(MIMEText(html_str,'html','utf-8'))
    data.attach(img)


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
