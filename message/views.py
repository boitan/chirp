from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from message.forms import RegisterForm


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = "/"


class TimelineView(ListView):
    template_name = 'index.html'
    def get_queryset(self):
        # implement the logic
        pass