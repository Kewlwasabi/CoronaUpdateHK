import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import password as p

def smtp_gmail(subject, body):
    username = "Kewlwasabi@gmail.com"
    password = p.getPass()
    smtp_server = "smtp.gmail.com"
    email_from = "CoronaUpdateHK"
    email_to = "tsou.c@husky.neu.edu"

    msg = MIMEMultipart()
    msg['From'] = email_from
    msg['To'] = email_to
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))


    server = smtplib.SMTP(smtp_server, 587)
    server.starttls()
    server.login(username, password)
    text = msg.as_string()
    server.sendmail(email_from, email_to, text)
    server.quit()
