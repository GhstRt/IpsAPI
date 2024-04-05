# from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    #    path('admin/', admin.site.urls),
    #path('login/', Login, name='login'),
    path('api/', include('api.urls'))
]
