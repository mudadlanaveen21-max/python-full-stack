'''
python project

SMTP (simple mail transfer protocol)
-----------------------------------
-----> this is used to send emails from server to another....

NOte :
----
1)  SMTP SSL Port
-----------------
465

2)SMTP TLS port
---------------
587

import smtplib

EmailMessage Class
------------------
msg['Subject'] = 'SMTP ON MAIL'
msg['From'] = 'sender@mail.com'
msg['To'] = 'Receiver@mail.com'

import smtplib
from email.message import EmailMessage
sender = 'mudadlaharsha@gmail.com'
password = 'yamimpjfywgvbanc'
msg = EmailMessage()

msg['Subject'] = 'Welcome mail'
msg['From'] = sender
msg['To'] = 'varshita060125@gmail.com'

msg.set_content('hai')
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender,password)
server.send_message(msg)
server.quit()

import smtplib
from email.message import EmailMessage

sender = 'mudadlaharsha@gmail.com'
password = 'fxoxlpolpighjbgn'
receiver_ = ['varshita060125@gmail.com','trishaakalisetti@gmail.com']
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender,password)
for email in receiver_:
    msg = EmailMessage()

    msg['Subject'] = 'Welcome Mail'
    msg['From'] = sender
    msg['To'] = email
    msg.set_content('cuties')

    server.send_message(msg)
server.quit()
