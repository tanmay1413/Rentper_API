from allauth.account.adapter import DefaultAccountAdapter
from django.template.loader import render_to_string
from .utils import send_email_async

class CustomAccountAdapter(DefaultAccountAdapter):
    def send_mail(self, template_prefix, to_email, context):
        subject = render_to_string(f"{template_prefix}_subject.txt", context).strip()
        body = render_to_string(f"{template_prefix}_message.txt", context)
        from_email = self.get_from_email()
        send_email_async(subject, body, from_email, [to_email])
