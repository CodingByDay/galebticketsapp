from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("", views.home, name="home"),
    # Create new ticket.
    path("create/", views.create, name="create"),
    # Comment.
]
