from django.urls import path
from . import views

urlpatterns = [
    path('',views.staffPanel,name='staffPanel'),
    path('products/', views.show_products, name='show_products'), 
    path('product/<int:product_id>/',views.increase_price, name='increase_price'), 
]