import os
from django.core.mail import EmailMultiAlternatives

from django.core.mail import send_mail

os.environ['DJANGO_SETTINGS_MODULE'] = 'logintest.settings'

if __name__ == '__main__':
    #send_mail('测试1','测试django','17607315498@163.com',['395368517@qq.com'])
    subject, from_email, to = '测试邮件', '17607315498@163.com', '395368517@qq.com'
    text_content = '欢迎访问www.baidu.com'
    html_content = '<p>欢迎访问站点<a href="http://www.baidu.com" target=_blank>http://www.baidu.com</a></p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()