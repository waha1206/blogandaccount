from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from . forms import MyUserCreationForm

# Create your views here.

#
@login_required
def dashboard(request):
    return render(request, 'account2/dashboard.html', locals())

def register(request):
    if request.method == 'POST':
        user_form = MyUserCreationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password1']
            )
            new_user.save()
            return render(
                request,
                'account2/register_done.html',
                locals()
            )
    else:
        user_form = MyUserCreationForm()
    return render(
        request,
        'account2/register.html',
        locals()
    )
