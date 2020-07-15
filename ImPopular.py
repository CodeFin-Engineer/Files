import sys
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import time
email = sys.argv[1]
amount = int(sys.argv[2])
delay = int(sys.argv[3])


email_user = 'theswiss.g@gmail.com'
email_password = 'codefin333'
email_send = email

subject = 'Keys:'+ str(datetime.datetime.today())

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

body = 'INFO:'
msg.attach(MIMEText(body,'plain'))


text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,email_password)

for i in range(amount):
    time.sleep(delay)
    server.sendmail(email_user,email_send,text)
server.quit()
