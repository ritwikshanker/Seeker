import smtplib


def sendMail(message, email_user):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587  # for smtp.gmail.com
    from_address = "generatortestcase@gmail.com"  # e.g. username@gmail.com
    from_password = "8192161998"  # required by script to login using your username
    to_address = email_user  # e.g. username2@gmail.com
    mail_body = message
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(from_address, from_password)
    server.sendmail(from_address, to_address, str(mail_body))
    server.quit()
