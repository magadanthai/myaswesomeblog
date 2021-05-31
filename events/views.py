from django.shortcuts import render


def home(requests):
    return render(requests, r'events\home.html')
