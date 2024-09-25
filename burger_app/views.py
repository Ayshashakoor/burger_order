from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import MenuItem, ContactMessage
from .forms import ContactForm


def home(request):
    products = MenuItem.objects.all()
    return render(request, 'home.html', {'products': products})


def menu_view(request):
    products = MenuItem.objects.all()
    return render(request, 'menu.html', {'products': products})


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:
            try:
                contact_message = ContactMessage(name=name, email=email, message=message)
                contact_message.save()
                messages.success(request, 'Your message has been sent!')
                return redirect('contact')
            except Exception as e:
                messages.error(request, 'There was an error sending your message. Please try again.')
        else:
            messages.error(request, 'All fields are required.')

    return render(request, 'contact.html')


def add_to_cart(request, item_id):
    item = get_object_or_404(MenuItem, id=item_id)
    cart = request.session.get('cart', {})

    if str(item_id) in cart:
        cart[str(item_id)]['quantity'] += 1
    else:
        cart[str(item_id)] = {
            'name': item.name,
            'price': str(item.price),
            'quantity': 1,
            'image': item.image.url
        }

    request.session['cart'] = cart
    return redirect('menu')


def view_cart(request):
    cart = request.session.get('cart', {})
    cart_items = [
        {
            'id': item_id,
            'name': item['name'],
            'price': item['price'],
            'quantity': item['quantity'],
            'image': item['image'],
            'total_price': float(item['price']) * item['quantity']
        }
        for item_id, item in cart.items()
    ]
    total = sum(item['total_price'] for item in cart_items)

    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total': total
    })


def update_cart(request, item_id, action):
    cart = request.session.get('cart', {})

    if str(item_id) in cart:
        if action == 'increment':
            cart[str(item_id)]['quantity'] += 1
        elif action == 'decrement':
            if cart[str(item_id)]['quantity'] > 1:
                cart[str(item_id)]['quantity'] -= 1
            else:
                del cart[str(item_id)]

        request.session['cart'] = cart

    return redirect('cart')


def clear_cart(request):
    if 'cart' in request.session:
        del request.session['cart']
    messages.success(request, 'Your cart has been emptied.')
    return redirect('cart')


def order_now(request):
    # Render the place order page
    return render(request, 'place_order.html')


def payment(request):
    if request.method == 'POST':
        # You can capture order details here if needed
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        city = request.POST.get('city')
        postal_code = request.POST.get('postal_code')

        # Store any necessary details in the session or process as needed
        request.session['order_details'] = {
            'name': name,
            'phone': phone,
            'address': address,
            'city': city,
            'postal_code': postal_code,
        }

        cart = request.session.get('cart', {})
        total_price = sum(float(item['price']) * item['quantity'] for item in cart.values())
        request.session['total_price'] = total_price
        context = {
            'total_price': total_price,
            'order_details': request.session['order_details'],  # Pass order details if needed
        }

        return render(request, 'payment.html', context)

    # If not a POST request, redirect back to the order page
    return redirect('order_now')

    
def payment_success(request):
    total_price = request.session.get('total_price', 0)
    return render(request, 'payment_success.html', {
        'total_price': total_price
    })


def process_payment(request):
    # Logic for processing payment (e.g., via PayPal) goes here
    return redirect('payment_success')
