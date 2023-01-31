import os

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# class Hashtag(models.Model):
#     name = models.CharField(max_length=30, related_name="name_hashtag", db_table="users_hashtags")

def user_directory_path_for_profile(instance, filename):
    return 'user_{0}/profile/{1}'.format(instance.user.id, filename)

def user_directory_path_for_post(instance, filename):
    return 'user_{0}/post/{1}'.format(instance.user.id, filename)

def get_upload_to(prefix):
    def _tmp(instance, filename):
        return os.path.join(instance.pk, prefix, filename)
    return _tmp


class Posts(models.Model):
    user = models.ForeignKey(User, related_name="user_post", on_delete=models.CASCADE, blank=True)
    image = models.ImageField(upload_to=user_directory_path_for_post, blank=True, null=True)
    name = models.TextField(max_length=1000)
    time_created = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    # hashtags = models.ManyToManyField(Hashtag)

    class Meta:
        verbose_name_plural = 'Posts'


class Comments(models.Model):
    author = models.ForeignKey(User, related_name="user_comment", on_delete=models.CASCADE, null=True)
    post = models.ForeignKey('Posts', on_delete=models.CASCADE, null=True)
    comment = models.TextField(max_length=500)
    time_created = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Comments'


class Likes(models.Model):
    post = models.ForeignKey('Posts', related_name="liked_post", on_delete=models.CASCADE)
    profile_id = models.ForeignKey(User, related_name="user_like", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Likes'


# class UsersProfile(models.Model):
#     GENDER = (
#         ('M', 'Man'),
#         ('W', 'Woman'),
#         ('N', 'None'),
#     )
#
#     user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
#     gender = models.CharField(max_length=1, choices=GENDER, default='N')
#     bio = models.TextField(max_length=1000, blank=True)
#     avatar = models.ImageField(upload_to=user_directory_path_for_profile, null=True, blank=True)
#     time_created = models.DateTimeField(auto_now_add=True)
#     time_update = models.DateTimeField(auto_now=True)
#     followers = models.ManyToManyField("self", blank=True)
#     following = models.ManyToManyField("self", blank=True)
#
#     def __str__(self):
#         return self.user

    # def get_absolute_url(self):
    #     return reverse('posts', kwargs={'user_name': self.user})

class Profile(models.Model):
    GENDER = (
        ('M', 'Man'),
        ('W', 'Woman'),
        ('N', 'None'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    gender = models.CharField(max_length=1, choices=GENDER, default='N')
    bio = models.TextField(max_length=1000, blank=True)
    avatar = models.ImageField(upload_to=user_directory_path_for_profile, null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    followers = models.ManyToManyField("self", blank=True)
    following = models.ManyToManyField("self", blank=True)

    def __str__(self):
        return self.user






