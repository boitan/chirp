# Create your views here.
from django.contrib.auth.models import User
from django.shortcuts import render

from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from message.forms import RegisterForm
from message.models import Message


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = "/login"

class TimelineView(ListView):
    template_name = 'index.html'
    def get_queryset(self):
        # implement the logic
        if self.request.user.is_authenticated:
            return Message.objects.filter(user=self.request.user)
        else:
            return Message.objects.all()

class ProfileBaseView(DetailView):
    model = User
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileBaseView, self).get_context_data(**kwargs)
        context["chirps"] = Message.objects.filter(user=self.get_object())
        return context

class MyProfileView(ProfileBaseView):
    def get_object(self, queryset=None):
        return self.request.user

class ProfileView(ProfileBaseView):
    def get_slug_field(self):
        return "username"

def follow_user(request, username):
    user = get_object_or_404(User, username=username)
    try:
        follow = Follow(followed_user=user, following_user=request.user)
        follow.save()
        messages.info(request, "You are now following {0}".format(username))
    except IntegrityError:
        messages.error(request, "You are already following this user")
    return redirect('profile', username)

def unfollow_user(request, username):
    user = get_object_or_404(User, username=username)
    try:
        follow = Follow.objects.filter(followed_user=user, following_user=request.user).first()
        follow.delete()
        messages.info(request, "You are no longer following {0}".format(username))
    except IntegrityError:
        messages.error(request, "You are already following this user")
    return redirect('profile', username)

def new_chirp(request):
    if request.method == "POST":
        form = MessageForm(data=request.POST)
        if form.is_valid():
            form.save()
    return redirect("index")