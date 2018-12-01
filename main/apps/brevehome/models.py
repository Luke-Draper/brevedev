from __future__ import unicode_literals
from django.db import models
import re

class UserManager(models.Manager):
    pass

class GroupManager(models.Manager):
    pass

class EventManager(models.Manager):
    pass

class LocationManager(models.Manager):
    pass

class CommentManager(models.Manager):
    pass

class User(models.Model):
    first_name = models.CharField(max_length=255)
    desc = models.CharField(max_length=1023)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=512)
    birthday = models.DateTimeField()
    linkedin_url = models.CharField(max_length=255)
    facebook_url = models.CharField(max_length=255)
    instagram_url = models.CharField(max_length=255)
    youtube_url = models.CharField(max_length=255)
    twitter_url = models.CharField(max_length=255)
    blog_url = models.CharField(max_length=255)
    public = models.BooleanField()
    friends = models.ManyToManyField('self')
    profile_picture = models.BinaryField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

class Group(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=1023)
    email = models.CharField(max_length=255)
    public = models.BooleanField()
    owner = models.ForeignKey(User, related_name='groups_owned')
    invitees = models.ManyToManyField(User, related_name='group_invitations')
    applicants = models.ManyToManyField(User, related_name='group_applications')
    members = models.ManyToManyField(User, related_name='groups_joined')
    profile_picture = models.BinaryField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = GroupManager()

class Event(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    date = models.DateTimeField()
    capacity = models.IntegerField()
    public = models.BooleanField()
    creator = models.ForeignKey(User, related_name='events_owned')
    invitees = models.ManyToManyField(User, related_name='events_invited')
    possible_attendees = models.ManyToManyField(User, related_name='events_might_attend')
    attendees = models.ManyToManyField(User, related_name='events_attending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = EventManager()

class Location(models.Model):
    name = models.CharField(max_length=255)
    street1 = models.CharField(max_length=255)
    street2 = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    event = models.ForeignKey(Event, related_name='location')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = LocationManager()

class Comment(models.Model):
    creator = models.ForeignKey(User, related_name='comments')
    content = models.CharField(max_length=255)
    message = models.ForeignKey(Event, related_name='messages')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CommentManager()
