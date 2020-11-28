import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender_address = "bot.boisko.agh@gmail.com"
sender_password = '2dpvKJ!%BL%E6FV%'
sender_name = "Bot Boisko MS-AGH"

def send_email(address, subject, text):
    message = MIMEText(text)

    message['Subject'] = subject
    message['From'] = str(Header(f"{sender_name} <{sender_address}>"))
    message['To'] = address
    
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(sender_address, sender_password)
    server.sendmail(sender_name, address, message.as_string())
    server.close()