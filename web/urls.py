from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework import routers

from website.views import ViewLoginMail
from api.views import *


router = routers.DefaultRouter()

router.register(r'get_registers', GetRegisterView, 'get')
router.register(r'post_registers', PostRegisterView, 'post')


urlpatterns = [
    path('', ViewLoginMail.as_view(), name="login"),
    path('api/', include((router.urls, 'api'), namespace='api')),
    path('admin/', admin.site.urls, name="admin"),
]


urlpatterns += staticfiles_urlpatterns()
