from django.shortcuts import render, redirect
from .models import Product,Review
from django.shortcuts import get_object_or_404

# Create your views here.
def home(request):
    return render(request, 'shop/home.html')

def contactus(request):
    return render(request, 'shop/contactus.html')

def products(request):
    products = Product.objects.all()
    return render(request, 'shop/products.html', {'products': products})


def p_details(request, product_id): 
    product = Product.objects.get(id=product_id) 
    return render(request, 'shop/p_details.html', {'product' : product})  

def by_category(request, category=None):
    if category:
        products = Product.objects.filter(category=category)
        return render(request, 'shop/by_category.html', {
            'products': products,
            'category': category,
        })       

def reviews(request):
    # Fetch all saved reviews from DB
    comments = Review.objects.all()

    if request.method == 'POST':
        username = request.POST.get('username')  #Get the submitted data
        comment = request.POST.get('comment')

        if username and comment:
            # Save to database
            Review.objects.create(username=username, comment=comment)
            return redirect('reviews')  # Prevent duplicate form resubmission

    return render(request, 'shop/reviews.html', {'comments': comments})

def delete_post(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    review.delete()
    return redirect('reviews')


