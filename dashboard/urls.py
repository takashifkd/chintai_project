from django.urls import path

from . import views

app_name = 'dashboard'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('property/list/', views.PropertyListView.as_view(), name="list"),
    path('property/detail/<int:pk>/',
         views.PropertyDetailView.as_view(), name="detail"),
    path('property/create/', views.PropertyCreateView.as_view(), name="create"),
    path('property/update/<int:pk>/',
        views.PropertyUpdateView.as_view(), name="update"),
    path('property/delete/<int:pk>/',
        views.PropertyDeleteView.as_view(), name="delete"),
]
