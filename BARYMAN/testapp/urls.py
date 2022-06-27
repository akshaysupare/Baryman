from django.urls import path, include
from testapp import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('product/', views.product_view, name='product'),
    path('one/', views.one_view, name='product'),
    path('half/', views.half_view, name='product'),         
]
