from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Follow, Like, Comment, Post, Profile

# Create your views here.

@login_required(login_url='/accounts/login')
def home(request):
    current_user = request.user


    title = 'Home'

    following = Follow.get_following(current_user.id)

    posts = Post.get_posts()

    # comments = Comment.get_post_comments()

    following_posts = []

    for follow in following:

        for post in posts:

            if follow.profile == post.profile:
                following_posts.append(post)

    # to allow us to view other user's profiles


    profiles = Profile.get_other_profiles(current_user.id)

    following = Follow.objects.filter(user=current_user)

    following_profile_list = []

    for follow in following:
        following_profile_list.append(follow.profile)

    profiles_list = []

    for profile in profiles:

        if profile not in following_profile_list:
            profiles_list.append(profile)

    return render(request, 'all_gram/home.html',
                  { "title": title, "following": following, "user": current_user, "posts": posts, "following_posts": following_posts, "profiles":profiles_list})