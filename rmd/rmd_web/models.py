from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Define your models here

class Person(models.Model):
    # Model for storing information about a person
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    instagram = models.CharField(max_length=100, blank=True, null=True)  # Optional Instagram handle
    joined_date = models.DateField(null=True)  # Date when the person joined the platform

class Post(models.Model):
    # Model for storing posts associated with a person
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  # User who created the post
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)  # Person associated with the post
    content = models.TextField(default='')  # Content of the post
    how_met = models.CharField(max_length=100, null=True)  # How the user met the person
    agree = models.IntegerField(default=0)  # Number of agreements on the post
    disagree = models.IntegerField(default=0)  # Number of disagreements on the post
    created_at = models.DateTimeField(default=timezone.now, editable=False, blank=True)  # Date and time when the post was created

    def save(self, *args, **kwargs):
        # Override save method to set created_at when the post is first saved
        if not self.pk:
            self.created_at = timezone.now()
        return super(Post, self).save(*args, **kwargs)

class Comment(models.Model):
    # Model for storing comments on posts
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)  # Post that the comment belongs to
    comment_date_created = models.DateField(null=True)  # Date when the comment was created
    agree = models.CharField(max_length=255)  # Agree on the comment
    disagree = models.IntegerField(null=True)  # Disagree on the comment
