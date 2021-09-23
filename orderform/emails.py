from django.template import Context
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings


def send_order_email(first_name, email, review):

    context = {
        'name': first_name,
        'email': email,
        'review':  review,
    }

    email_subject = 'Thank you for your order!'
    email_body = render_to_string('email_message.txt', context)

    email = EmailMessage(
        email_subject, email_body,
        settings.DEFAULT_FROM_EMAIL, [email, ])
    return email.send(fail_silently=False)