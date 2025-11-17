from decimal import Decimal
from django.shortcuts import render,redirect
from shop.models import Product
from django.shortcuts import get_object_or_404

# Create your views here.
def staffPanel(request):
    return render(request, 'staff/staffpanel.html')

def show_products(request): 
    products = Product.objects.all() 
    return render(request, 'staff/staffpanel.html', {'products': products}) 

def increase_price(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Increase price by 300
    product.price += Decimal('300.00')
    product.save()  # Save change to database
    # Redirect back to the staff dashboard or product list

    return redirect('show_products')  # make sure this URL shows all products