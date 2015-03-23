from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from datetime import datetime


class Street(models.Model):
    name = models.CharField(max_length=128)
    average_safety_rate = models.IntegerField(default=0)
    average_business_rate = models.IntegerField(default=0)
    average_infrastructure_rate = models.IntegerField(default=0)
    average_rate = models.IntegerField(default=0)
    location = models.CharField(max_length=128, unique=True)
    image = models.ImageField(upload_to='', blank=True)
    slug = models.SlugField(default=True)

    def save(self, *args, **kwargs):
                self.slug = slugify(self.name)
                super(Street, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class Comment(models.Model):
    street = models.ForeignKey(Street)
    user = models.ForeignKey(User)
    comment = models.CharField(max_length=128)
    agree = models.IntegerField(default=0)
    disagree = models.IntegerField(default=0)
    safety_rate = models.IntegerField(default=0)
    business_rate = models.IntegerField(default=0)
    infrastructure_rate = models.IntegerField(default=0)
    rate = models.IntegerField(default=0)
    time = models.DateTimeField(default=datetime.now(), null=True)

    def __unicode__(self):
        return self.comment


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    # telephone = models.IntegerField(max_length=128, blank=True)
    picture = models.ImageField(upload_to='profile_images', default= 'profile_images/head.png',blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username