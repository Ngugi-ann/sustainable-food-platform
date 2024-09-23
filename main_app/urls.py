from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    # Detail views for farmers, processors, and distributors
    path('farmer/<int:pk>/', views.farmer_detail, name='farmer_detail'),
    path('processor/<int:pk>/', views.processor_detail, name='processor_detail'),
    path('distributor/<int:pk>/', views.distributor_detail, name='distributor_detail'),
    
    # Order views for farmer, processor, and distributor products
    path('order/farmer/<int:farmer_id>/', views.order_product, name='order_farmer'),
    path('order/processor/<int:processor_id>/', views.order_product, name='order_processor'),
    path('order/distributor/<int:distributor_id>/', views.order_product, name='order_distributor'),
    
    # Success page after an order
    path('success/', views.order_success, name='order_success'),
    
    # Consumer dashboard and profile creation
    path('dashboard/', views.consumer_dashboard, name='consumer_dashboard'),
    path('create-consumer-profile/', views.create_consumer_profile, name='create_consumer_profile'),
    
    # Logout view
    path('logout/', views.logout, name='logout'),
]
