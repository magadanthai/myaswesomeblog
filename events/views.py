from django.shortcuts import render
from .models import Main


def home(request):
    events = Main.objects
    return render(request, r'events\home.html', {'events': events})
