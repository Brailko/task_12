from django.conf.urls import handler404
from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseServerError, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from .forms import *
from .models import *


def index(request):
    users = User.objects.exclude(username=request.user) & User.objects.exclude(is_staff=True)
    return render(request, "posts/index.html", {"users": users, "title": "Title"})

def show_post(request, post_id):
    post = get_object_or_404(Posts, pk=post_id)
    user = User.objects.get(username=post.user)
    comments = Comments.objects.filter(post=post.pk)
    return render(request, "posts/post.html", {"title": "Post", "post": post, "user": user, "comments": comments})

def show_profile_and_post(request, username):

    if not User.objects.filter(username=username):
        raise Http404()
    user = User.objects.get(username=username)
    posts = Posts.objects.filter(user=user.pk)

    return render(request, "posts/profile_and_post.html", {"user": user, "posts": posts})

def create_post(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()
    return render(request, "posts/create_post.html", {"form": form, "title": "Create post"})

# def create_profile(request):
#     if request.method == 'POST':
#         form = AddProfileForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.instance.user = request.user
#             form.save()
#             return redirect('home')
#     else:
#
#         form = AddProfileForm()
#     return render(request, "posts/edit_profile.html", {"form": form, "title": "Create profile"})

def pageNotFound(request, exeption):
    text_page_not_found = '<h1>Sorry, this page is unavailable.</h1>' \
                              '<p></p>' \
                              '<p>You may have used an invalid link or the page has been removed.</p>' \
                              '<p>Back to <a href="http://127.0.0.1:8000/">DjangoGramm</a></p>'
    return HttpResponseNotFound(text_page_not_found)

def custom_handler500(request):
    text_page_not_found = '<h1>Sorry, this page is unavailable.</h1>' \
                              '<p></p>' \
                              '<p>You may have used an invalid link or the page has been removed.</p>' \
                              '<p>Back to <a href="http://127.0.0.1:8000/">DjangoGramm</a></p>'
    return HttpResponseServerError(text_page_not_found)


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'posts/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        Profile.objects.create(user=user)
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'posts/login.html'

    def get_success_url(self):
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('login')


class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'posts/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context


class UserEditView(UpdateView):
    model = EditProfileForm
    template_name = 'posts/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


class EditProfilePageView(UpdateView):
    model = Profile
    template_name = 'posts/edit_profile_page.html'
    form_class = ProfileForm

    success_url = reverse_lazy('home')

