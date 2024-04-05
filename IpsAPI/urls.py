# from django.contrib import admin
from django.urls import path

from api.views.Login import Login

urlpatterns = [
    #    path('admin/', admin.site.urls),
    path('login/', Login, name='login'),
]
