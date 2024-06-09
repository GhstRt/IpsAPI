from django.urls import path
from api.views import *

urlpatterns = [
    path('login/', Login.as_view(), name='login'),

    path('get-rules/', GetRules.as_view(), name='get-rules'),
    path('get-rules/<int:rule_id>/', GetRules.as_view(), name='get-rules'),
    path('add-rule/', AddRule.as_view(), name='add-rule'),
    path('update-rule/<int:rule_id>/', UpdateRule.as_view(), name='update-rule'),
    path('delete-rule/<int:rule_id>/', DeleteRule.as_view(), name='delete-rule'),

    path('get-users/', GetUsers.as_view(), name='get-users'),
    path('get-users/<int:user_id>/', GetUsers.as_view(), name='get-users'),
    path('add-user/', AddUser.as_view(), name='add-user'),
    path('update-user/<int:user_id>/', UpdateUser.as_view(), name='update-user'),

    path('get-logs/', GetLogs.as_view(), name='get-logs'),
    path('get-logs/<int:log_id>/', GetLogs.as_view(), name='get-logs'),
    path('add-log/', AddLog.as_view(), name='add-log'),

    path('get-alerts/', GetAlerts.as_view(), name='get-alerts'),

    path('get-status/', GetStatus.as_view(), name='get-status')
]
