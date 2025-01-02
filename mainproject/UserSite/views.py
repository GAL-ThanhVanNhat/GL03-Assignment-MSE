from django.shortcuts import render
from django.http import HttpResponse

from .models import User

# Create your views here.
def index(request):
    users = User.objects.all()
    context = {"users": users}
    return render(request, 'user_site/index.html', context)
