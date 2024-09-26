from django.urls import path
from .views import Homepage, Signup, Login

app_name = 'lib_app'

urlpatterns = [
    path('home/', Homepage.as_view(), name='home'),
    path('signup/', Signup.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
]