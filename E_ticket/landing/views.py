from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse , reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView,CreateView,UpdateView,DetailView,DeleteView,View,TemplateView
#from .models import Blog,Comment,Like,Love
#from .forms import CommentForm
#import uuid

# Create your views here.



class ElectronicVoting(LoginRequiredMixin, TemplateView):
    template_name = 'landing/index.html'
