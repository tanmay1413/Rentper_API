from .tasks import send_email

def send_email_async(subject, message, from_email, recipient_list):
    send_email.delay(subject, message, from_email, recipient_list)
