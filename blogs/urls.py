from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path("control-panel/", views.control_panel, name="control_panel"),
    path("add-blog/", views.add_blog, name="add_blog"),
    path("delete/<int:id>", views.delete_blog, name="delete_blog"),
    path("update/<int:id>", views.update_blog, name="update_blog"),
    path("diaries/", views.diaries, name="diaries"),
    path("detail/<int:id>", views.detail, name="detail"),
    path("add-comment/<int:id>", views.add_comment, name="add_comment"),
    path("delete-comment/<int:id>/<int:id2>", views.delete_comment, name="delete_comment"),
    path("surf/", views.surf, name="surf"),
]
