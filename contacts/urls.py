from django.urls import path
from .views import ContactCreateView, MessageListCreate, UserList, chat_view

urlpatterns = [
    path('contacts/', ContactCreateView.as_view(), name='contact-create'),
    path('messages/', MessageListCreate.as_view(), name='message-list-create'),
    path('users/', UserList.as_view(), name='user-list'),
    path('', chat_view, name='chat'),
]
