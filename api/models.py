from django.db import models

# Create your models here.
class Bucketlist(models.Model):
    ''' this is the bucketlist model, never really had a legit bucketlist '''
    name = models.CharField(max_length=255, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.name)
#ok so to test the test .... u get what i mean.. cmd is python manage.py test
