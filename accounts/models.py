from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):

    phone = models.CharField(max_length=15,unique=True)


class UserProfile(models.Model):

    dob = models.DateField(null=True)

    bio = models.TextField(null=True)

    GENDER_CHOICES=(
        ("male","male"),
        ("female","female"),

    )

    gender = models.CharField(max_length=200,choices=GENDER_CHOICES,default="male")

    profile_picture = models.ImageField(upload_to="profile_pictures",null=True)

    owner = models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")



def create_profile(sender,instance,created,**kwargs):

    if created:

        UserProfile.objects.create(owner = instance)

from django.db.models.signals import post_save

post_save.connect(create_profile,sender=User)


from django.core.mail import send_mail

def send_email_notification(sender,instance,created,**kwargs):

    if created:

        send_mail(
                    subject="account invitation",
                    from_email="sajaykannan10@gmail.com",
                    recipient_list=["donalddixon246@gmail.com"],
                    message="your blog post account created")

post_save.connect(send_email_notification,sender=User)