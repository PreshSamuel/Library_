from django.urls import path
from .views import HomePage

app_name = 'lib_app'

urlpatterns = [
    path('home/', HomePage.as_view(), name='home'),
]