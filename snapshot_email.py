#!/usr/bin/python

import smtplib, sys
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

image_file = sys.argv[1]
to_email_addr = sys.argv[2]
outlook_user = ''
outlook_password = ''

msg = MIMEMultipart()
msg['From'] = outlook_user
msg['To'] = to_email_addr
msg['Date'] = formatdate(localtime=True)
msg['Subject'] = "Hello from Martin\'s Raspberry Pi 2"
msg.attach( MIMEText('Here is your photo.') )

with open(image_file, "rb") as fil:
	part = MIMEApplication(
		fil.read(),
		Name=basename(image_file)
	)
	part['Content-Disposition'] = 'attachment; filename="%s"' % basename(image_file)
	msg.attach(part)

smtpserver = smtplib.SMTP('smtp-mail.outlook.com',587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(outlook_user, outlook_password)
smtpserver.sendmail(outlook_user, to_email_addr, msg.as_string())
smtpserver.quit()
