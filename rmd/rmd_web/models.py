from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# import uuid
# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    instagram = models.CharField(max_length=100, blank=True, null=True)
    joined_date = models.DateField(null=True)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)
    content = models.TextField(default='')
    how_met = models.CharField(max_length=100, null=True)
    agree = models.IntegerField(default=0)
    disagree = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now, editable=False, blank=True)  # Set default value to current date and time

    def save(self, *args, **kwargs):
        if not self.pk:
            self.created_at = timezone.now()
        return super(Post, self).save(*args, **kwargs)
    
# class Post(models.Model):
#     # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     user_id = models.IntegerField(null=True)
#     person_id = models.IntegerField(null=True)
#     person_firstname = models.CharField(max_length=255)
#     person_lastname = models.CharField(max_length=255)
#     post = models.CharField(max_length=255)
#     agree = models.IntegerField(null=True)
#     disagree = models.IntegerField(null=True)
#     comments = models.CharField(max_length=255)
    
class Comment(models.Model):
    post_id = models.IntegerField(null=True)
    comment_date_created = models.DateField(null=True)
    agree = models.CharField(max_length=255)
    disagree = models.IntegerField(null=True)