
from django.conf import settings
from django.core.mail import send_mail

def mail_for_changing_password(mail, token):
    """ send the mail for changing password """
    subject = '[好市好事]更改密碼'
    message = f'您好, 更改密碼連結 http://127.0.0.1:8000/login/change-password/{token}'
    send_mail(subject, message, settings.EMAIL_HOST_USER, [mail])
    return True


def mail_for_token_verification(email, token):
    """ send the verify mail for register """
    subject: str = '[好市好事]帳號驗證'
    message: str = f'請點擊連結認證帳號 http://127.0.0.1:8000/login/verify/{token}'
    send_mail(subject, message, settings.EMAIL_HOST_USER, [email])



