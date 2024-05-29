from django.urls import path
from . import views
from .views import master_signup, client_signup, user_login

urlpatterns = [
    path('main/', views.main, name='home'),
    path('serif/', views.serif, name='serif'),
    path('o_nas/', views.o_nas, name='o_nas'),
    path('message/', views.message, name='message'),
    path('signup/master/', master_signup, name='master_signup'),
    path('signup/client/', client_signup, name='client_signup'),
    path('login/', user_login, name='login'),
]
