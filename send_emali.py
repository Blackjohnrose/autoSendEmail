# - *- coding: utf- 8 - *-

import smtplib 
import config

def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRES, config.PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(config.EMAIL_ADDRES, config.EMAIL_TARGET, msg)
        server.quit()
        print("success: send email!")
    except:
        print("Email Filed to send!")    

subject = "Re: hi"
msg = "write some text"

send_email(subject, msg)
