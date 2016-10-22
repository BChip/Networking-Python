import smtplib

mailServ = smtplib.SMTP('smtp.gmail.com:587')
mailServ.ehlo()
mailServ.starttls()

username = raw_input('Enter your Gmail username: ')
password = raw_input('Enter your Gmail password: ')

try:
	mailServ.login(username,password)
except smtplib.SMTPAuthenticationError:
	print "Invalid Username or Password!"
	mailServ.quit()	
	exit()

to = raw_input('To: ')
subject = raw_input('Subject: ')
text = raw_input('Message: ')

msg = 'Subject: %s\n\n%s' % (subject, text)

try:
	mailServ.sendmail(username,to,msg)
except Exception:
	print "Could not send mail!"
	mailServ.quit()
	exit()

print "Message successfully sent!"
mailServ.quit()
