from django.urls import path
from api.views import *

urlpatterns = [
    path('login/', Login.as_view(), name='login')
]
