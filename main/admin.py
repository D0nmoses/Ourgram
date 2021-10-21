from django.contrib import admin
from .models import Like, Follow, Post, Profile, Tag, Comment


admin.site.register(Like)
admin.site.register(Follow)
admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Tag)
admin.site.register(Comment)