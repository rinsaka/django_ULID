from django.urls import path

# from . import views
from .views import CommentIndexView

app_name = 'comments'
urlpatterns = [
    path('', CommentIndexView.as_view(), name='index'),
]
