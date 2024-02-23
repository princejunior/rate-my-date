from django.contrib import admin

# Register your models here.
from .models import Person, Post, Comment

# Register your models here.
# admin.site.register(User)
admin.site.register(Person)
admin.site.register(Post)
admin.site.register(Comment)
