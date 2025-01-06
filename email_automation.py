import smtplib
from email.mime.text import MIMEText

def send_email(to_address, subject, message):
    from_address = 'sendemail131@gmail.com'
    password = 'bsav lhkw ybrw agmx'

    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = from_address
    msg['To'] = to_address

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
         server.login(from_address, password)
         server.sendmail(from_address, to_address, msg.as_string())

# Example usage
send_email('cruzdante099@gmail.com', 'Elective', 'Email send successful')
