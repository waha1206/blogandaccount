from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

app_name = 'account2'
urlpatterns = [
    # path('login/', views.user_login, name='login'),
    path('login/', auth_views.LoginView.as_view(template_name='account2/login.html'), name='login'),
    path('', views.dashboard, name='dashboard'),
    path('logout/', auth_views.LogoutView.as_view(template_name='account2/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('<str:username>', views.profile, name='profile'),
    # path(
    #     'password-change/',
    #     auth_views.PasswordChangeView.as_view(
    #         template_name='account2/password_change.html'
    #     ),
    #     name='password_change'
    # ),
    path('password-change/',
        auth_views.PasswordChangeView.as_view(
            success_url=reverse_lazy('account2:password_change_done')
        ),
        name='password_change'),
    path(
        'password-change-done/',
        auth_views.PasswordChangeDoneView.as_view(
            template_name='account2/password_change_done.html'
        ),
        name='password_change_done'
    ),
]
