from django.shortcuts import render, redirect
from .forms import MasterSignUpForm
from .forms import ClientSignUpForm
from .models import Master, Client
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm


def main(request):
    return render(request, 'main.html')


def serif(request):
    return render(request, 'serif.html')


def o_nas(request):
    return render(request, 'o_nas.html')


def message(request):
    return render(request, 'message.html')


def about(request):
    return render(request, 'main/about.html')


def master_signup(request):
    if request.method == 'POST':
        form = MasterSignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            Master.objects.create(
                user=user,
                contact_phone=form.cleaned_data.get('contact_phone'),
                specialization=form.cleaned_data.get('specialization'),
                photo=form.cleaned_data.get('photo')
            )
            login(request, user)
            return redirect('home')
    else:
        form = MasterSignUpForm()
    return render(request, 'registrations_master.html', {'form': form})


def client_signup(request):
    if request.method == 'POST':
        form = ClientSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            Client.objects.create(
                user=user,
                contact_phone=form.cleaned_data.get('contact_phone'),
                address=form.cleaned_data.get('address')
            )
            login(request, user)
            return redirect('home')
    else:
        form = ClientSignUpForm()
    return render(request, 'registrations_client.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'user/login.html', {'form': form})


