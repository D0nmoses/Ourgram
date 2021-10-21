from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Follow, Post, Profile, Comment, Like
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from .forms import NewPostForm, NewCommentForm

# Create your views here.

@login_required(login_url='/accounts/login/')
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

    return render(request, 'all-posts/home.html',
                  { "title": title, "following": following, "user": current_user, "posts": posts, "following_posts": following_posts, "profiles":profiles_list})


@login_required(login_url='/accounts/login/')
def profile(request,id):
    '''	
    View function to display the profile of the logged in user when they click on the user icon	
    '''
    current_user = request.user

    try:

        single_profile = Profile.objects.get(user=current_user.id)

        title = f'{current_user.username}\'s'

        posts = Post.objects.filter(user=current_user.id)

        return render(request, 'all-posts/my_profile.html', {"title":title,"single_profile":single_profile,"current_user":current_user,"posts":posts})

    except ObjectDoesNotExist:
        raise Http404()

@login_required(login_url='/accounts/login')
def new_post(request):
    '''	
    View function to display a form for creating a post to a logged in authenticated user 	
    '''
    current_user = request.user

    current_profile = current_user.profile

    if request.method == 'POST':

        form = NewPostForm(request.POST, request.FILES)

        if form.is_valid:

            post = form.save(commit=False)

            post.user = current_user

            post.profile = current_profile

            post.save()

            return redirect(profile, current_user.id)

    else:

        form = NewPostForm()

    title = 'Create Post'

    return render(request,'all-posts/new_post.html', {"form":form})

@login_required(login_url='accounts/login/')
def new_comment(request, id):
    '''
    View function to display a form for creating a comment on a post
    '''
    current_user = request.user

    current_post = Post.objects.get(id=id)

    if request.method == 'POST':

        form = NewCommentForm(request.POST)

        if form.is_valid:
            comment = form.save(commit=False)

            comment.user = current_user

            comment.post = current_post

            comment.save()

            return redirect(home, current_post.id)

    else:

        form = NewCommentForm()

    title = f'Comment {current_post.user.username}\'s Post'

    return render(request, 'all-posts/new_comment.html', {"title": title, "form": form, "current_post": current_post})

@login_required(login_url='/accounts/login')
def follow(request,id):
    '''	
    View function to add a profile to the current user's follow list
    '''
    current_user = request.user

    follow_profile = Profile.objects.get(id=id)

    following = Follow(user=current_user, profile=follow_profile)

    following.save()

    return redirect(home)

@login_required(login_url='/accounts/register')
def post(request,id):
    '''	
    View function to display a single post, its comments and likes	
    '''
    current_user = request.user
    try:
        current_post = Post.objects.get(id=id)

        title = f'{current_post.user.username}\'s post'

        comments = Comment.get_post_comments(id)

        likes = Like.num_likes(id)

        like = Like.objects.filter(post=id).filter(user=current_user)

    except ObjectDoesNotExist:
        raise Http404()

    return render(request, 'all-posts/post.html', {"title":title, "post":current_post,"comments":comments,"likes":likes,"like":like })

@login_required(login_url='/accounts/login')
def like(request,id):
    '''	
    View function add a like to a post the current user has liked	
    '''
    current_user = request.user

    current_post = Post.objects.get(id=id)

    like = Like(user=current_user,post=current_post,likes_number=1)

    like.save()

    return redirect(post,current_post.id)