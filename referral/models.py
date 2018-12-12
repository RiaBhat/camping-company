from django.db import models
from django.db.models.signals import pre_save
from django.contrib.auth.models import User
from .utils import unique_slug_generator


class Referral(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.slug

    def __unicode__(self):
        return self.slug


def referral_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator()


pre_save.connect(referral_pre_save_receiver, sender=Referral)