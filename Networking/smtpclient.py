## create a smtp client that will send email from python script to gmail account. For this we are using gmail server as a smtp server.

import smtplib
from email.mime.text import MIMEText

body="test email"
msg=MIMEText(body)          # will contain the body, subject etc
msg['From']="username@gmail.com"
msg['To']="user2@gmail.com"
msg['Subject']="hello"

server=smtplib.SMTP('smtp.gmail.com',587)    ## create a smtp object with smtp server details
server.starttls()                               ## start a secure connection
server.login("username@gmail.com", "password")    # email id and password
server.send(msg)

print("mail sent")

server.quit()

