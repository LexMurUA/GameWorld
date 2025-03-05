from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Review
from .forms import ReviewForm
from products.models import Product

@login_required  
def add_review(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user 
            review.product = product  
            review.save()
            return redirect("product_detail", product_id=product.id)  

    else:
        form = ReviewForm()

    return render(request, "reviews/add_review.html", {"form": form, "product": product})
