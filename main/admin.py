from django.contrib import admin

from main.models import Post, Comment

admin.site.register([Post, Comment])
