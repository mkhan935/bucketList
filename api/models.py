from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
# Create your models here.
class Bucketlist(models.Model):
    ''' this is the bucketlist model, never really had a legit bucketlist '''
    name = models.CharField(max_length=255, blank=False, unique=True)
    owner = models.ForeignKey('auth.User',
        related_name='bucketlists',
        on_delete = models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.name)
#ok so to test the test .... u get what i mean.. cmd is python manage.py test

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
