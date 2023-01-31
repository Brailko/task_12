from django.contrib import admin

from .models import *

# class UsersProfileAdmin(admin.ModelAdmin):
#     list_display = ('id', 'user', 'avatar', 'time_created')
#     list_display_links = ('id', 'user',)
#     search_fields = ('username',)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'avatar', 'time_created')
    list_display_links = ('id', 'user',)
    search_fields = ('user',)

class PostsAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'time_created')
    list_display_links = ('user', 'name',)
    search_fields = ('user',)

class CommentsAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'comment', 'time_created')
    list_display_links = ('author', 'post',)
    search_fields = ('author', 'post',)

# admin.site.register(UsersProfile, UsersProfileAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Posts, PostsAdmin)
admin.site.register(Comments, CommentsAdmin)


