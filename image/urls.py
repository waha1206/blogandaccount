from django.urls import path
from . import views

app_name = 'image'
urlpatterns = [
    path('upload/', views.image_upload, name='image_upload'),
	path('list/', views.image_list, name='image_list'),
	path('<int:id>/<str:slug>/', views.image_detail, name='image_detail'),
]