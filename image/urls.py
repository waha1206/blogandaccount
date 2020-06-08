from django.urls import path
from . import views

app_name = 'image'
urlpatterns = [
    path('upload/', views.image_upload, name='image_upload'),
	path('list/', views.image_list, name='image_list'),
	path('<int:id>/<str:slug>/', views.image_detail, name='image_detail'),
	path('like/<int:id>', views.image_like, name='image_like'),
	path('unliike/<int:id>', views.image_unlike, name='image_unlike'),
]