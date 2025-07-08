from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('signup/', views.signup, name='signup'),
    path('Comercial/', views.Commercial, name='Commercial'),
    path('Domestic/', views.Domestic, name='Domestic'),
    path('login/', views.login, name='login'),
    path('buffalows/', views.buffalows, name='buffalows'),
    path('cows/', views.cows, name='cows'),
    path("order/", views.order_form, name="order_form"),
    path("order-success/", views.order_success_view, name="order_success"),
]