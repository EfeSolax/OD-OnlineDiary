from django.contrib import admin
from django.urls import path, include

from blogs import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name = "main_page"),
    path("about/", views.about, name = "about"),
    path("user/", include("user.urls")),
    path("blogs/", include("blogs.urls")),
]
