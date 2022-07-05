from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six
from django.conf import settings

# imports for sending email start
from django.core.mail import get_connection, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
# imports for sending email end

class tokengenerator(PasswordResetTokenGenerator):

	def _make_hash_value(self, subscriber, timestamp):
		return six.text_type(subscriber.pk)+six.text_type(timestamp)+six.text_type(subscriber.is_verified)

generate_token = tokengenerator()

def send_auto_email(receiver, subject, template, context, request):

    mail_content = render_to_string(template, context)
    mail_text = strip_tags(mail_content)
    email_from = settings.EMAIL_HOST_USER
    connection = get_connection() # uses SMTP server specified in settings.py
    connection.open()                                   
    msg = EmailMultiAlternatives(subject, mail_text, email_from, receiver, connection=connection)                                      
    msg.attach_alternative(mail_content, "text/html")
    msg.send()
    connection.close()