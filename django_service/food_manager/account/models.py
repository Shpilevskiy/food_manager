import uuid
from django.db import models
from django.utils import timezone


def default_expire_date():
    return timezone.now() + timezone.timedelta(days=10)


def generate_new_link():
    return uuid.uuid4().hex


class InviteLink(models.Model):
    link = models.CharField(max_length=120, unique=True,
                            default=generate_new_link)
    creation_date = models.DateField(default=timezone.now)
    expire_date = models.DateTimeField(default=default_expire_date)
    activation_count = models.PositiveSmallIntegerField(default=3)


class Company(models.Model):
    title = models.CharField(max_length=120, null=False)
    description = models.CharField(max_length=3100)
    invite_link = models.OneToOneField(InviteLink, on_delete=models.CASCADE)
