from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.conf import settings

def reg_mail():
    # user=User.objects.filter(username=username)
    # email=user[0].email
    send_mail(
    "Reg mail",
    "Here is the message.",
    settings.EMAIL_HOST_USER,
    ["gouravchahar1111@gmail.com"],
    )
    
def delete_mail():
    # user=User.objects.filter(username=username)
    # email=user[0].email
    send_mail(
    "del mail",
    "Here is the message.",
    settings.EMAIL_HOST_USER,
    ["gouravchahar1111@gmail.com"],
    )