from django.contrib.auth.models import User
from rest_framework import generics, permissions
from .models import Contact, Message
from .serializers import ContactSerializer, MessageSerializer, UserSerializer
from django.shortcuts import render


def chat_view(request):
    return render(request, 'chat.html')


class ContactCreateView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class MessageListCreate(generics.ListCreateAPIView):
    queryset = Message.objects.all().order_by('-timestamp')
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
