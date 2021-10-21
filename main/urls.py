from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('', views.home, name='home'),
    re_path(r'^profile/(\d+)', views.profile, name="profile"),
    re_path(r'^create/post', views.new_post, name="new-post"),
    re_path(r'^follow/(\d+)', views.follow, name="follow"),
    re_path(r'^create/comment/(\d+)', views.new_comment, name="new_comment"),
    re_path(r'^like/(\d+)', views.like, name="like"),
    re_path(r'^post/(\d+)', views.post, name="post"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)