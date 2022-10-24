from django.shortcuts import render
from .models import Sword
from cart.models import Cart

# Create your views here.

#Home Page
def home(request):
    #Retrieve Sword Objects and their Details
    swords = Sword.objects.all()
    context = {'swords' : swords}
    return render(request, 'home-page.html', context)

def product(request, slug):
    sword = Sword.objects.get(slug=slug)
    context = {'sword_item' : sword}
    return render(request, 'product-page.html', context)

def cart_add(request, slug): #, quantity): #We'll deal with the quantities later 
    cart = Cart(request)
    sword = Sword.objects.get(slug=slug)
    cart.add(product=sword)
    context = {'sword_item' : sword}
    return render(request, 'product-page.html', context)

#Checkout Page
def cart_detail(request):
    context = {}
    if request.method == 'POST': #'Place Order' button was clicked
        cart = request.session
        cart.clear()
        context = {'message' : 'Order Successfully Placed!'}
    return render(request, 'checkout-page.html', context)

def cart_clear(request):
    cart = request.session
    cart.clear()
    return render(request, 'checkout-page.html')



























#Add Items to the Cart
# def add_to_cart(request, slug):
#     item = get_object_or_404(Sword, slug=slug)
#     order_item, created = Cart.objects.get_or_create(
#         item=item,
#         user=request.user
#     )
#     order_qs = Order.objects.filter(user=request.user, ordered=False)
#     if order_qs.exists():
#         order = order_qs[0]
#         # check if the order item is in the order
#         if order.orderitems.filter(item__slug=item.slug).exists():
#             order_item.quantity += 1
#             order_item.save()
#             messages.info(request, "This item quantity was updated.")
#             return redirect(reverse(home), order_item.quantity)
#         else:
#             order.orderitems.add(order_item)
#             messages.info(request, "This item was added to your cart.")
#             return redirect(reverse(home), order_item.quantity)
#     else:
#         order = Order.objects.create(
#             user=request.user)
#         order.orderitems.add(order_item)
#         messages.info(request, "This item was added to your cart.")
#         return redirect(reverse(home), order_item.quantity)



# #Remove Items from the Cart
# def remove_from_cart(request, slug):
#     item = get_object_or_404(Sword, slug=slug)
#     cart_qs = Cart.objects.filter(user=request.user, item=item)
#     if cart_qs.exists():
#         cart = cart_qs[0]
#         # Checking the cart quantity
#         if cart.quantity > 1:
#             cart.quantity -= 1
#             cart.save()
#         else:
#             cart_qs.delete()
#     order_qs = Order.objects.filter(
#         user=request.user,
#         ordered=False
#     )
#     if order_qs.exists():
#         order = order_qs[0]
#         # check if the order item is in the order
#         if order.orderitems.filter(item__slug=item.slug).exists():
#             order_item = Cart.objects.filter(
#                 item=item,
#                 user=request.user,
#             )[0]
#             order.orderitems.remove(order_item)
#             messages.info(request, "This item was removed from your cart.")
#             return redirect(reverse(home))
#         else:
#             messages.info(request, "This item was not in your cart")
#             return redirect(reverse(home))
#     else:
#         messages.info(request, "You do not have an active order")
#         return redirect(reverse(home))
