from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, AddProductForm
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticatedUser, allowed_users
import json

@login_required(login_url='login')
def store(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0,'get_cart_items':0}
        cartItems = order['get_cart_items']
    products = Product.objects.all()
    context = {'products': products, 'cartItems':cartItems}
    return render(request, 'store/store.html', context)

@login_required(login_url='login')
def cart(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0,'get_cart_items':0}
    context = {'items':items, 'order': order,'cartItems':cartItems}
    return render(request, 'store/cart.html', context)
@login_required(login_url='login')
def checkout(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0,'get_cart_items':0}
    context = {'items':items, 'order': order,'cartItems':cartItems}
    return render(request, 'store/checkout.html', context)


@login_required(login_url='login')
@allowed_users
def dashboard(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        orderitems = OrderItem.objects.all()
        UserOrders = []
        pendingOrders = []
        deleveredOrders = []
        for i in range(len(orderitems)):
            if orderitems[i].product.manager_id == request.user:
                UserOrders.append(orderitems[i])
                if orderitems[i].status == 'Pending':
                    pendingOrders.append(orderitems[i])
                if orderitems[i].status == 'Delevered':
                    deleveredOrders.append(orderitems[i])
        totalOrders = len(UserOrders)
        pending = len(pendingOrders)
        delevered = len(deleveredOrders)
        items = []
        order = {'get_cart_total':0,'get_cart_items':0}
    context = {'items':items, 'order': order,'cartItems':cartItems,'UserOrders':UserOrders,'totalOrders':totalOrders,'delevered':delevered,'pending':pending}
    return render(request, 'store/dashbord.html', context)


@unauthenticatedUser
def loginPage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('store')
        else:
            messages.info(request, 'username or password is incorrect')
            return redirect('login')

    context = {'request':request}
    return render(request, 'store/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')

@unauthenticatedUser
def register(request):
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Account was created for "+user)
            return redirect('login')

    context = {'form': form}
    return render(request, 'store/register.html', context)

@login_required(login_url='login')
def updateItem(request):
    data = json.loads(request.body.decode("utf-8"))
    productId = data['productId']
    action = data['action']
    
    print('ProductId ',productId)
    print('action ',action)

    customer = request.user
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer,complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity += 1
    elif action == 'remove':
        orderItem.quantity -= 1
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()    

    return JsonResponse("Item was added", safe=False)


@login_required(login_url='login')
@allowed_users
def orders(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        orderitems = OrderItem.objects.all()
        UserOrders = []
        pendingOrders = []
        deleveredOrders = []
        for i in range(len(orderitems)):
            if orderitems[i].product.manager_id == request.user:
                UserOrders.append(orderitems[i])
                if orderitems[i].status == 'Pending':
                    pendingOrders.append(orderitems[i])
                if orderitems[i].status == 'Delevered':
                    deleveredOrders.append(orderitems[i])
        print(pendingOrders)
        totalOrders = len(UserOrders)
        pending = len(pendingOrders)
        delevered = len(deleveredOrders)
        
        
        items = []
        order = {'get_cart_total':0,'get_cart_items':0}
    context = {'items':items, 'order': order,'cartItems':cartItems,'UserOrders':UserOrders,'delevered':delevered,'pending':pending}
    return render(request, 'store/orders.html',context)

@login_required(login_url='login')
@allowed_users
def addProduct(request):
    form = AddProductForm(request.POST,request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            obj = form.save(commit=False)
            obj.manager_id = request.user
            obj.save()
            messages.success(request,"product was added successfully")
            return redirect('addproduct')

            
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0,'get_cart_items':0}
    context = {'items':items, 'order': order,'cartItems':cartItems,'form':form}
    return render(request, 'store/addproduct.html',context)

def processOrder(request):
    data = json.loads(request.body)
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        order.complete = True
        print(order)
        order.save()

        ShippingAddress.objects.create(customer=customer,
        order=order, 
        address=data['shipping']['address'], 
        city=data['shipping']['city'],
        state=data['shipping']['state'],
        zipcode=data['shipping']['zipcode']
        )
    return JsonResponse("Payment Complete", safe=False)
