from django.contrib import admin
from django.urls import path
from website.api.views import RegisterView
from website.views import ViewLoginMail

urlpatterns = [
    path('', ViewLoginMail.as_view(), name="login"),
    path('registers/', RegisterView.as_view(), name="registers"),
    path('admin/', admin.site.urls, name="registers"),
]
