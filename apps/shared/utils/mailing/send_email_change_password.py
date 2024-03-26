from django.template.loader import render_to_string

from apps.shared.mails.mail_helpers import send_mail
from apps.users.models import User


def send_email_change_password(user: User):
    to_email = [user.email]
    context = {
        "activation_code": user.activation_code,
    }
    message = render_to_string('mailing/forgot_password.html', context)

    send_mail(
        subject="Ваш пароль был сброшен | Your password has been reset",
        message=message,
        recipient_list=to_email,
    )
