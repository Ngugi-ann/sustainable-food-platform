from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib import messages
from .models import Farmer, Processor, Distributor, Consumer, Product, Order
from .forms import ContactForm, OrderForm, ConsumerProfileForm, UserRegistrationForm, UserLoginForm

# Index view to display all stakeholders, handle login, and registration
def index(request):
    farmers = Farmer.objects.all()
    processors = Processor.objects.all()
    distributors = Distributor.objects.all()
    contact_form = ContactForm()

    registration_form = UserRegistrationForm()
    login_form = UserLoginForm()

    if request.method == 'POST':
        if 'register' in request.POST:
            registration_form = UserRegistrationForm(request.POST)
            if registration_form.is_valid():
                user = registration_form.save()
                auth_login(request, user)  # Auto-login after registration
                messages.success(request, "Registration successful. Welcome!")
                return redirect('index')
            else:
                messages.error(request, "Registration failed. Please check the form for errors.")
        
        elif 'login' in request.POST:
            login_form = UserLoginForm(request, data=request.POST)
            if login_form.is_valid():
                user = login_form.get_user()
                auth_login(request, user)
                messages.success(request, "Login successful!")
                return redirect('index')
            else:
                messages.error(request, "Login failed. Please check your credentials.")

    form = None
    if request.user.is_authenticated:
        if not Consumer.objects.filter(user=request.user).exists():
            messages.info(request, "You need to create or update your profile.")
            form = ConsumerProfileForm()  # Display profile form if profile does not exist

    return render(request, 'main_app/index.html', {
        'farmers': farmers,
        'processors': processors,
        'distributors': distributors,
        'contact_form': contact_form,
        'registration_form': registration_form,
        'login_form': login_form,
        'form': form  # Pass the form to the template
    })

# Detail view for a specific farmer
def farmer_detail(request, pk):
    farmer = get_object_or_404(Farmer, pk=pk)
    return render(request, 'main_app/farmer_detail.html', {'farmer': farmer})

# Detail view for a specific processor
def processor_detail(request, pk):
    processor = get_object_or_404(Processor, pk=pk)
    return render(request, 'main_app/processor_detail.html', {'processor': processor})

# Detail view for a specific distributor
def distributor_detail(request, pk):
    distributor = get_object_or_404(Distributor, pk=pk)
    return render(request, 'main_app/distributor_detail.html', {'distributor': distributor})

# View for ordering a product, with payment options
@login_required
def order_product(request, farmer_id=None, processor_id=None, distributor_id=None):
    try:
        consumer = Consumer.objects.get(user=request.user)
    except Consumer.DoesNotExist:
        messages.error(request, "You need to create a profile before placing an order.")
        return redirect('create_consumer_profile')

    # Ensure you fetch the correct stakeholder (Farmer, Processor, or Distributor)
    farmer = get_object_or_404(Farmer, pk=farmer_id) if farmer_id else None
    processor = get_object_or_404(Processor, pk=processor_id) if processor_id else None
    distributor = get_object_or_404(Distributor, pk=distributor_id) if distributor_id else None

    # Filter products based on the stakeholder
    if farmer:
        products = Product.objects.filter(farmer=farmer)
    elif processor:
        products = Product.objects.filter(processor=processor)
    elif distributor:
        products = Product.objects.filter(distributor=distributor)
    else:
        products = Product.objects.none()

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.consumer = consumer
            order.save()  # Save the order

            messages.success(request, "Order placed successfully!")
            return redirect('order_success')
        else:
            messages.error(request, "Failed to place the order. Please check the form.")
    else:
        form = OrderForm()

    return render(request, 'main_app/order_form.html', {
        'form': form,
        'farmer': farmer,
        'processor': processor,
        'distributor': distributor,
        'products': products  # Pass filtered products to the template
    })

# Success page after an order is placed
def order_success(request):
    return render(request, 'main_app/order_success.html')

# Consumer dashboard view
@login_required
def consumer_dashboard(request):
    orders = Order.objects.filter(consumer__user=request.user)
    return render(request, 'main_app/consumer_dashboard.html', {'orders': orders})

# Create or update consumer profile view
@login_required
def create_consumer_profile(request):
    if Consumer.objects.filter(user=request.user).exists():
        return redirect('consumer_dashboard')

    if request.method == 'POST':
        form = ConsumerProfileForm(request.POST)
        if form.is_valid():
            consumer_profile = form.save(commit=False)
            consumer_profile.user = request.user
            consumer_profile.save()
            messages.success(request, "Profile created successfully!")
            return redirect('consumer_dashboard')
        else:
            messages.error(request, "Profile creation failed. Please check the form.")
    else:
        form = ConsumerProfileForm()

    return render(request, 'main_app/create_profile.html', {'form': form})

# Logout view
@login_required
def logout(request):
    auth_logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('index')
