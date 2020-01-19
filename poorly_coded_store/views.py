from django.shortcuts import render, redirect
from .models import Product, Order
from django.db.models import Sum

def index(request):
    context = {
        "all_products":Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    context = {
        'order': Order.objects.last(),
        'total_quantity_of_all_orders': Order.objects.aggregate(Sum('quantity_ordered')),
        'total_charge_for_all_orders': Order.objects.aggregate(Sum('total_price')),
    }
    return render(request, "store/checkout.html", context)

def calculations(request):
    product = Product.objects.get(id=request.POST['product_id'])
    price_from_form = product.price
    quantity_from_form = int(request.POST["quantity"])
    total_charge = quantity_from_form * price_from_form
    Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    return redirect('/checkout')

# def checkout(request):
#     context = {
#         'order': Order.objects.last(),
#         'total_quantity_of_all_orders': Order.objects.aggregate(Sum('quantity_ordered')),
#         'total_charge_for_all_orders': Order.objects.aggregate(Sum('total_price')),
#     }
#     quantity_from_form = int(request.POST["quantity"])
#     price_from_form = float(request.POST["price"])
#     total_charge = quantity_from_form * price_from_form
#     print("Charging credit card...")
#     Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
#     return render(request, "store/checkout.html", context)    ## modified line due to adding context dictionary above
    # return render(request, "store/checkout.html")         ## original line