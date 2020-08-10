# OnlineNurseryMarketPlace
## This is an Online Ecommerce Nursery Markert Place where a Nursery Manager or owner can sell his products and a User say customer can buy these products.
# Main Features
## 1. The application is build on the basis of role base access control where in the Nursery Manager can Add Products and Manage Orders. While as the user can only buy the products.
## 2. The application has a shopping cart that gets updated in real time as soon as the user presses Add To Cart while as the quantity of a particular product can be also updated inside the cart.

# Setup
First make sure you have python 3 installed on you system.
To be able to use the project you first need to clone the repository

```bash
git clone https://github.com/towseef41/OnlineNurseryMarketPlace.git
```
you can also download it form
```bash
https://github.com/towseef41/OnlineNurseryMarketPlace.git
```

 After cloning the project open the folder is your desired code editor and open the terminal in the current directory

Type
```bash
pip -m venv demo
```
then
```bash
cd demo/Scripts
```
```bash
 activate
```
This will activate the virtual environmnment. Now again go to the root directiory of the folder i,e OnlineNurseryMarkertPlace then type
```bash
  pip install -r requirements.txt
```
After everything is installed successfully.In the same root directory type
```bash
 python manage.py runserver
```
The development sever will be at 
```bash
 http://127.0.0.1:8000/
```
If everything worked fine you will be redirected to login page

# Usage
There are two ways to register your account one is as user i,e customer and another is as nursery owner.

If you want to register as a nursery manager then you have to check the option of "Are You a Nursery Owner".

After registering login with the username and password.

The nursery manager has a dashboard in which he can Add Product, View Orders, and also Manage Them.

If you register as customer the you want be able to see these features but you can view products add them to cart also Proceed to Checkout.

After checkout the order will be reflected on the particular nursery managers dashboard who had added that product.


