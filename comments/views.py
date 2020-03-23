# from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic import ListView
from .models import Comment

# Create your views here.


class CommentIndexView(ListView):
    model = Comment
