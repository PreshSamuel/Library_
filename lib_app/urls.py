from django.urls import path
from .views import Homepage

app_name = 'lib_app'

urlpatterns = [
    path('home/', Homepage.as_view(), name='home'),
]