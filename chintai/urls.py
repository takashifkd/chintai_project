from django.urls import path

from . import views

app_name = 'chintai'
urlpatterns = [
    path('', views.index, name="index"),
    path('inquiry/', views.inquiry_form, name="inquiry"),
]
