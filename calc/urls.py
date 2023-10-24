from django.urls import path
from.import views
urlpatterns=[
    path('',views.home,name='home'),
    path('add',views.add, name='add'),
    path('dashboard',views.dashboard, name='dashboard'),
    path('products',views.products, name='products'),
    path('customer/<str:pk_test>/',views.customer, name='customer'),
] 