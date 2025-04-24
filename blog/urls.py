from django.urls import path

from blog.views import *

urlpatterns = [
    path("", PostView.as_view(), name="home"),
    path("<slug:slug>/", view=PostDetail.as_view(), name="post_detail"),
]
