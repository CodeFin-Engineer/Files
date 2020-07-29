import sys
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#------ Will make it headless-----------
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)




amount = int(sys.argv[2])
delay = int(sys.argv[3])
emails = sys.argv[1].split(',')
for i in range (len(emails)):
    emails[i] = emails[i].strip('(')
    emails[i] = emails[i].strip(')')
    area = str(emails[i][0:3])
    firstpart = str(emails[i][5:8])
    secondpart = str(emails[i][9:len(emails[i])])
    emails[i] = area+firstpart+secondpart

    driver.get("http://www.fonefinder.net/")
    driver.find_element_by_xpath("/html/body/table[1]/tbody/tr/td[2]/table/tbody/tr[3]/td[1]/input").send_keys(area)
    driver.find_element_by_xpath("/html/body/table[1]/tbody/tr/td[2]/table/tbody/tr[3]/td[2]/input[1]").send_keys(
        firstpart)
    driver.find_element_by_xpath("/html/body/table[1]/tbody/tr/td[2]/table/tbody/tr[3]/td[2]/input[2]").send_keys(
        secondpart)
    driver.find_element_by_xpath("/html/body/table[1]/tbody/tr/td[2]/table/tbody/tr[3]/td[3]/input").click()
    provider = driver.find_element_by_xpath("/html/body/center[1]/table[2]/tbody/tr[2]/td[5]/a")
    if "T-MOBILE" in provider.text:
        emails[i] = "1" + area + firstpart + secondpart + "@tmomail.net"  # Works
    elif "VERIZON WIRELESS" in provider.text:
        emails[i] = area + firstpart + secondpart + "@vtext.com"  # Works
    elif "SPRINT" in provider.text:
        emails[i] = area + firstpart + secondpart + "@messaging.sprintpcs.com"
    elif "CINGULAR WIRELESS" in provider.text:
        emails[i] = area + firstpart + secondpart + "@txt.att.net"


#driver.close()
#----------------------------------------------

email_user = 'analert.message@gmail.com'
email_password = 'C0D3F!N333'
email_send = emails

subject = 'SPAM!'

msg = MIMEMultipart()
#msg['From'] = email_user
msg['To'] = ", ".join(email_send)
msg['Subject'] = subject

body = '>:D'
msg.attach(MIMEText(body,'plain'))


text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,email_password)

for i in range(amount):
    time.sleep(delay)
    server.sendmail(email_user,email_send,text)
server.quit()
