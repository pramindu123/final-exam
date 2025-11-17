from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('contactus',views.contactus,name='contactus'),
    path('products',views.products,name='products'),
    path('reviews',views.reviews,name='reviews'),
    path('product/<int:product_id>/',views.p_details, name='p_details'), 
    path('product/<str:category>/', views.by_category, name='by_category'), 
    path('delete/<int:review_id>/', views.delete_post,name='delete_post'),
]
