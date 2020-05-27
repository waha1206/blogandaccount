from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


@login_required
def dashboard(request):
    return render(request, 'account2/dashboard.html', locals())
