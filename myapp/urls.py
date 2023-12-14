from django.urls import path
from . import views
from myapp import views  # Replace 'myapp' with the actual name of your app


urlpatterns = [
    path('api/customers/', views.CustomerListCreateView.as_view(), name='customer-list'),
    path('api/products/', views.ProductListCreateView.as_view(), name='product-list'),
    path('api/orders/', views.OrderListCreateView.as_view(), name='order-list'),
    
    path('api/create-customer/', views.create_new_customer, name='create-customer'),

    path('api/create-product/', views.create_new_product, name='create-product'),

    path('api/create-order/', views.create_new_order, name='create-order'),

    
    
  
    
]
