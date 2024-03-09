from django.urls import path
from . import views
from .views import home,export_sales_to_excel



urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('home/',views.home,name = 'home'),
     path('export/<str:date>/', export_sales_to_excel, name='export_sales_to_excel'),
]
