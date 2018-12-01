from __future__ import unicode_literals
from django.db import models
import re

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        if len(postData['first_name']) < 0:
            errors["first_name"] = "First Name cannot be empty"
        if len(postData['last_name']) < 0:
            errors["last_name"] = "Last Name cannot be empty"
        if len(postData['email']) < 0:
            errors["email"] = "Email cannot be empty"
        if re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$',postData['email']) == None:
            errors["email"] = "Email format is invalid"
        if len(postData['password']) < 8:
            errors["password"] = "Password must have at least 8 characters"
        if len(postData['desc']) < 50:
            errors["desc"] = "Description must have at least 50 characters"
        

class GroupManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        if len(postData['name']) < 0:
            errors["name"] = "Name cannot be empty"
        if len(postData['desc']) < 50:
            errors["desc"] = "Description must have at least 50 characters"
        if len(postData['email']) < 0:
            errors["email"] = "Email cannot be empty"

class EventManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        if len(postData['name']) < 0:
            errors["name"] = "Name cannot be empty"
        if len(postData['desc']) < 50:
            errors["desc"] = "Description must have at least 50 characters"
        if postData['capacity'] < 0:
            errors["capacity"] = "Must include a capacity size"

class LocationManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        if len(postData['name']) < 0:
            errors["name"] = "Name cannot be empty"
        if len(postData['street1']) < 50:
            errors["street1"] = "Address field cannot be empty"
        if len(postData['city']) < 50:
            errors["city"] = "City cannot be empty"
        if len(postData['state']) < 50:
            errors["state"] = "State cannot be empty"
        if len(postData['zip_code']) < 50:
            errors["zip_code"] = "Zip Code cannot be empty"
        if len(postData['country']) < 50:
            errors["country"] = "Country cannot be empty"
        

class CommentManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        if len(postData['content']) < 0:
            errors["content"] = "Comment cannot be empty"

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=512)
    birthday = models.DateTimeField()
    desc = models.CharField(max_length=1023)
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
