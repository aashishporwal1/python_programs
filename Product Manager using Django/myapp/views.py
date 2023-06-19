from django.shortcuts import render, get_object_or_404
from .models import Product_mst , Product_sub_cat

def product_list(request):
    products = Product_mst.objects.all()
    return render(request, 'product_manager/product_list.html', {'products': products})

def product_detail(request, product_id):
    products = Product_sub_cat.objects.filter(pk=product_id)
    return render(request, 'product_manager/product_detail.html', {'products': products})

def product_update(request, product_id):
    product = get_object_or_404(Product_mst, pk=product_id)
    if request.method == 'POST':
        # Process form data and update the product
        # ...
        return redirect('product_detail', product_id=product_id)
    return render(request, 'product_manager/product_update.html', {'product': product})

def product_delete(request, product_id):
    product = get_object_or_404(Product_mst, pk=product_id)
    if request.method == 'POST':
        # Delete the product
        # ...
        return redirect('product_list')
    return render(request, 'product_manager/product_delete.html', {'product': product})

def product_search(request):
    query = request.GET.get('q')
    products = Product_mst.objects.filter(product_name__icontains=query)
    return render(request, 'product_manager/product_search.html', {'products': products})
