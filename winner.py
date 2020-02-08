# Import smtplib for the actual sending function
import smtplib
import pathlib
import json
# Import the email modules we'll need
from email.message import EmailMessage


def send_winner_mail(message):
    config = ""
    with open(str(pathlib.Path(__file__).parent) + '/config.json') as config_file:
        config = json.load(config_file)

    # Create a text/plain message
    msg = EmailMessage()

    fromAddr = "george.steel92@gmail.com"
    toAddr = "c.theo.kent@gmail.com"

    msg['Subject'] = f'Winner!! [URGENT]'
    msg['From'] = fromAddr
    msg['To'] = toAddr

    msg.set_content(message)

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()

    server.login(fromAddr, config['email_password'])
    server.sendmail(fromAddr, toAddr, msg.as_bytes())
    server.quit()