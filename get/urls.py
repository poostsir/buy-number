from django.urls import path
from .views import geting_code, geting_code_dev, turn_of_Or_on

urlpatterns = [
    path('code/<str:token>/',geting_code,name='code'),
    path('code-dev/<str:token>/',geting_code_dev,name='code-dev'),
]
