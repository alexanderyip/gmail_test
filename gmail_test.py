# -*- coding: utf-8 -*-
"""
Created on Wed Jan 08 14:06:31 2014

@author: ayip
"""

#testing email reads
import imaplib
user = 'XX'
pw = 'XX'
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(user,pw)
mail.select('inbox')
result,data=mail.uid('search',None,'All')
print data
result,data=mail.uid('fetch',data[0],'(RFC822)')
raw_email = data[0][1]

import email
email_msg = email.message_from_string(raw_email)
print email_msg.items()
mail.logout()

#testing email sends
import smtplib
server = smtplib.SMTP('smtp.gmail.com',port=587)
server.starttls()
server.ehlo()
server.login(user,pw)
sender = 'mullenpython@gmail.com'
recipient = 'mullenpython@gmail.com'
subject = 'test test'
headers = ["from: " + sender,
            "subject: " + subject,
            "to: " + recipient,
            "mime-version: 1.0",
            "content-type: text/html"]
header = '/r/n'.join(headers)
body = 'test'
server.sendmail(sender, recipient, header + "\r\n\r\n" + body)
server.quit()
server.close()
