from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, Tag, Post, Follow, Comment, Like

# Create your tests here.


class ProfileTestClass(TestCase):
    '''	
    Test case for the Profile class	
    '''
    def setUp(self):

        # Create instance of Profile class
        self.new_profile = Profile(bio="Trial case bio")

    def test_instance(self):

        self.assertTrue( isinstance(self.new_profile, Profile) )

    def test_get_profiles(self):

        gotten_profiles = Profile.get_profiles()

        profiles = Profile.objects.all()

        self.assertTrue(len(gotten_profiles) == len(profiles))

    def test_get_other_profiles(self):

        self.don = User(username="don")
        self.don.save()

        self.dan = User(username="dan")
        self.dan.save()

        self.test_profile = Profile(user=self.dan,bio="Another Trial")

        gotten_profiles = Profile.get_other_profiles(self.don.id)

        profiles = Profile.objects.all()

        self.assertTrue( len(gotten_profiles) < len(profiles))


class TagTestClass(TestCase):
    '''	
    Test case for Tag class	
    '''

    # Set Up method
    def setUp(self):

        # Create a Tag instance
        self.new_tag = Tag(name='Mombasa')

    def test_instance(self):

        self.assertTrue(isinstance(self.new_tag, Tag))

    def test_save_tag(self):

        self.new_tag.save_tag()

        gotten_tags = Tag.objects.all()

        self.assertTrue(len(gotten_tags) > 0)

    def test_delete_tag(self):

        self.new_tag.save_tag()

        gotten_tags = Tag.objects.all()

        self.new_tag.delete_tag()

        self.assertTrue(len(gotten_tags) == 0)

    def test_get_tags(self):

        self.new_tag.save_tag()

        gotten_tags = Tag.get_tags()

        existing_tags = Tag.objects.all()

        self.assertTrue(len(gotten_tags) == len(existing_tags))


class PostTestClass(TestCase):
    '''	
    Test case for the Post class	
    '''
    def setUp(self):

        # Create a Post instance
        self.new_post = Post(caption='Check out my killer abs')

    def test_instance(self):

        self.assertTrue(isinstance(self.new_post, Post))

    def test_get_posts(self):

        gotten_posts = Post.get_posts()

        posts = Post.objects.all()

        self.assertTrue(len(gotten_posts) == len(posts))

    def test_get_profile_posts(self):

        self.don = User(username="don")
        self.don.save()

        self.dan = User(username="dan")
        self.dan.save()

        self.test_profile = Profile(user=self.dan,bio="Test Profile")

        self.test_post = Post(user=self.dan,caption="Test post here")

        gotten_profile = Post.get_profile_posts(self.dan.id)

        profiles = Post.objects.all()

        self.assertTrue(len(gotten_profile) == len(profiles))