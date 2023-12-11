from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from decimal import Decimal  # Import Decimal
from django.contrib import messages
from django.urls import reverse  


def get_cart_info(request):
    cart = request.session.get('cart', {})
    cart_total = sum(cart.values())
    total_price = Decimal('0')

    for product_id, quantity in cart.items():
        product = Product.objects.get(pk=product_id)
        product_price = Decimal(str(product.price))
        total_price += product_price * Decimal(str(quantity))

    return cart_total, total_price


def update_cart(request, product_id):
    # Retrieve the product from the database
    product = Product.objects.get(pk=product_id)

    # Retrieve the cart from the session or create an empty cart
    cart = request.session.get('cart', {})

    print(request.POST)  # print request.POST for debugging

    # Get the action (increment or decrement)
    action = request.POST.get('action')

    print(f"Action: {action}")  # print the action for debugging

    # Convert product_id to string
    product_id_str = str(product_id)

    # Perform the action
    if action:
        if action == 'increment':
            cart[product_id_str] = cart.get(product_id_str, 0) + 1
        elif action == 'decrement':
            # Check if the product_id exists in the cart before decrementing
            if cart.get(product_id_str, 0) > 1:
                cart[product_id_str] = cart.get(product_id_str, 0) - 1
            else:
                # If the quantity is 1, remove the item from the cart
                del cart[product_id_str]

        # Save the updated cart to the session
        request.session['cart'] = cart

    return redirect('cart')


def store(request):
    products = Product.objects.all()

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('store')
    else:
        form = ProductForm()

    return render(request, 'store.html', {'products': products, 'form': form})

def cart(request):
    # Retrieve the cart from the session
    cart = request.session.get('cart', {})

    # Calculate the total quantity
    cart_total = sum(cart.values())

    # Retrieve product details for products in the cart
    cart_products = []
    total_price = Decimal('0')

    for product_id, quantity in cart.items():
        product = Product.objects.get(pk=product_id)
        product_price = Decimal(str(product.price))
        total_price += product_price * Decimal(str(quantity))
        cart_products.append({'product': product, 'quantity': quantity})

    return render(request, 'cart.html', {'cart_products': cart_products, 'total_price': total_price, 'cart_total': cart_total})

def add_to_cart(request, product_id):
    # Retrieve the product from the database
    product = Product.objects.get(pk=product_id)

    # Retrieve the cart from the session or create an empty cart
    cart = request.session.get('cart', {})

    # Add the product to the cart or increment the quantity
    cart[product_id] = cart.get(product_id, 0) + 1

    # Save the updated cart to the session
    request.session['cart'] = cart

    return redirect('store')

def checkout(request):
    # Retrieve the cart from the session
    cart = request.session.get('cart', {})

    # Gather information needed for the checkout process
    products_in_cart = []

    total_price = Decimal('0')  # Initialize total_price as Decimal

    for product_id, quantity in cart.items():
        product = Product.objects.get(pk=product_id)
        
        # Convert product.price to Decimal before multiplication
        product_price = Decimal(str(product.price)) * Decimal(quantity)
        total_price += product_price

        products_in_cart.append({
            'name': product.name,
            'quantity': quantity,
            'total_price': product_price,
        })

    context = {
        'products_in_cart': products_in_cart,
        'total_price': total_price,
    }

    return render(request, 'checkout.html', context)

def process_order(request):
    # Clear the cart after processing the order
    request.session['cart'] = {}
    # Assuming the order was successful
    success_message = "Your purchase was successful! Thank you for shopping with us."

    # success message to the Django messages framework
    messages.success(request, success_message)

    # Redirect to the success page with the success message as a query parameter
    success_page_url = reverse('success_page') + f'?message={success_message}'
    return redirect(success_page_url)

def success_page(request):
    success_message = request.GET.get('message', '')
    return render(request, 'success_page.html', {'success_message': success_message})

def remove_from_cart(request, product_id):
    # Retrieve the cart from the session
    cart = request.session.get('cart', {})

    # Convert product_id to string
    product_id_str = str(product_id)

    # Remove the product from the cart
    if product_id_str in cart:
        del cart[product_id_str]

    # Save the updated cart to the session
    request.session['cart'] = cart

    return redirect('cart')
