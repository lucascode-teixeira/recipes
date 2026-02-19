from django.urls import path
from apps.core.views import *

app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
]
