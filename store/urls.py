from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('dashboard/', views.dashboard, name='dashboard' ),
    path('orders/',views.orders,name='orders'),
    path('addproduct/', views.addProduct, name='addproduct'),
    path('processorder/', views.processOrder, name='processorder'),
    path('login/', views.loginPage, name='login'),
    path('register/',views.register,name='register'),
    path('update_item/',views.updateItem, name='update_item'),
    path('logout/',views.logoutUser,name='logout')
]
