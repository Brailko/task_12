from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('p/<int:post_id>/', show_post, name='post'),
    path('p/create/', create_post, name='create_post'),
    # path('p/create_profile/', create_profile, name='create_profile'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('<str:username>/', show_profile_and_post, name='profile_and_post'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('user_profile/<int:pk>/', ShowProfilePageView.as_view(), name='user_profile'),
    path('edit_profile_page/<int:pk>/', EditProfilePageView.as_view(), name='edit_user_profile'),

]