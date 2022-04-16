import json
import os

from sendgrid.helpers.mail import Mail
from flask import jsonify
import dotenv
from sendgrid.sendgrid import SendGridAPIClient
# from sendgrid import SendGridAPIClient

dotenv.load_dotenv()

REQUEST_TEMPLATE_ID = 'd-11b73a22d847453cb095523c3cfc2fc9'
CONFIRMATION_TEMPLATE_ID = 'd-d8b3aca8728c44d0af31bcc069e72c7a'
REJECTED_TEMPLATE_ID = 'd-c0af3a87b7994a29b26e261f00af8b92'


def send_mail(mail, template, json_data):
    message = Mail(
        from_email='elysiumproject2022@gmail.com',
        to_emails=mail)

    message.dynamic_template_data = json_data
    message.template_id = template
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.__cause__)


def send_rejected_mail(mail, name, admin_name, reason):
    json_data = {
        "name": name,
        "admin_name": admin_name,
        "reason": reason
    }
    send_mail(mail, REJECTED_TEMPLATE_ID, json_data)


def send_confirmation_mail(mail, name, admin_name):
    json_data = {
        "name": name,
        "admin_name": admin_name,
    }
    send_mail(mail, CONFIRMATION_TEMPLATE_ID, json_data)


def send_request_mail(mail, name):
    json_data = {
        "name": name,
    }
    send_mail(mail, REQUEST_TEMPLATE_ID, json_data)


if __name__ == "__main__":
    data = {
            'reason': "No accurate data"
        }
    send_rejected_mail('sidor.marian.andrei3001@gmail.com', "Sidor Andrei", "Loredana Stefania", "You are too noisy")

