from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('form/new/', views.create_form, name='form_new'),
    path('form/list/', views.form_list, name='form_list'),
    path('form/<int:pk>/', views.form_detail, name='form_detail'),
    path('form/<int:pk>/edit/', views.form_edit, name='form_edit'),
]