from django.db import models
import uuid
from django.contrib.auth.models import Group
# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE
from django.utils import timezone
from datetime import datetime
from django.utils.translation import ugettext_lazy as _
# Create your models here.


def logofile(instance, filename):
    return '/'.join( ['logo', str(instance.id), filename] )

class Category(models.Model):
    id =models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner =  models.CharField(max_length=200)
    name=  models.CharField(max_length=200)
    #models.ManyToManyField(Tag, related_name='posts', blank=True)
    description=  models.TextField()
    logo = models.ImageField(upload_to=logofile,null=True, blank=True)


class Organisation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner =  models.CharField(max_length=200)
    name=  models.CharField(max_length=200)
    #models.ManyToManyField(Tag, related_name='posts', blank=True)
    description=  models.TextField()
    logo = models.ImageField(upload_to=logofile,null=True, blank=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    #models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE, blank=True, null=True)


