from django.urls import path
from app import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path("", RedirectView.as_view(url="/login/")),
    path('register/', views.register, name='register'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('home/', views.home, name='home'),
    path('book/<int:pk>/', views.vaccineSlot, name='vaccineSlot'),
    path('delete/<int:pk>/', views.delete, name='del_center'),
    path('add/', views.add, name='add_center'),
]
