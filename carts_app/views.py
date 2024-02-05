from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View

from store_app.models import Product, Variation
from .models import Cart, CartItem

# Create your views here.

# put product without login also in card sections
# for card.html
def _card_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart






# add perticular item to card 
def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)  #get the product
    product_variation = []
    if request.method == 'POST':
        # for geting size and color of product from url
        for item in request.POST:
            key = item 
            value = request.POST[key]
            
            try:
                # geting product variation
                variation = Variation.objects.get(product=product, variation_category__iexact=key, variation_value__iexact=value)
                # ------
                product_variation.append(variation)
            except:
                pass
        # size = request.GET['size']
        
    
    try:
        cart = Cart.objects.get(cart_id=_card_id(request)) #get the cart using the cart_id present in the session
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _card_id(request)
        )
    cart.save()



    # check cart item exits or not then add 
    is_cart_item_exists = CartItem.objects.filter(product=product, cart=cart).exists()
    if is_cart_item_exists:
        cart_item = CartItem.objects.filter(product=product, cart=cart)  # return card items object
        # existting_variations -> database
        # current variation  -> product_variation
        # item_id    -> database

        ex_var_list = []
        id = []

        for item in cart_item:
            existing_variation = item.variations.all()
            ex_var_list.append(list(existing_variation))
            id.append(item.id)


        if product_variation in ex_var_list:
            # increase the cart item quantity
            index = ex_var_list.index(product_variation)
            item_id = id[index]
            item = CartItem.objects.get(product=product, id=item_id)
            item.quantity += 1
            item.save()

        else:
            # create a new cart item
            # --------variation card select 

            item = CartItem.objects.create(product=product, quantity=1, cart=cart)

            if len(product_variation) > 0:
                item.variations.clear() #each time new color and size will be taken
                item.variations.add(*product_variation)
            item.save()
    else:
        cart_item = CartItem.objects.create(
            product = product,
            quantity = 1,
            cart = cart,
        )  
        # --------variation card select 
        if len(product_variation) > 0:
            cart_item.variations.clear()
            cart_item.variations.add(*product_variation)
        cart_item.save()
    # return HttpResponse(cart_item.product)
    # exit()
    return redirect('cart')






# decrement items
class Remove_cart(View):
    def get(self,request, product_id, cart_item_id):
        cart = Cart.objects.get(cart_id = _card_id(request))
        product = get_object_or_404(Product, id=product_id)
        try:
            cart_item = CartItem.objects.get(product=product, cart=cart, id=cart_item_id)
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
                cart_item.save()
            else:
                cart_item.delete()
        except: 
            pass
        return redirect('cart')



# remove holl card perticuar
class Remove_cart_item(View):
    def get(self,request, product_id, cart_item_id):
        cart = Cart.objects.get(cart_id = _card_id(request))
        product = get_object_or_404(Product, id=product_id)
        cart_item = CartItem.objects.get(product=product, cart=cart, id=cart_item_id)
        cart_item.delete()
        return redirect('cart')

class Cartt(View):
    template_name = "store/cart.html"
    def get(self,request, total=0, quantity=0, cart_items=None):
        try:
            tax=0
            grand_total=0
            cart = Cart.objects.get(cart_id=_card_id(request))
            cart_items = CartItem.objects.filter(cart=cart, is_active=True)
            for cart_item in cart_items:
                total += (cart_item.product.price * cart_item.quantity)
                quantity += cart_item.quantity
            tax = (2 * total)/100
            grand_total = total + tax

        except ObjectDoesNotExist:
            pass

        context = {
            'total' : total,
            'quantity': quantity,
            'cart_items': cart_items,
            'tax'       : tax,
            'grand_total': grand_total,
        } 
        return render(request, self.template_name, context)



# creating checkout page 
class Checkout(View):
    template_name = "store/checkout.html"
    def get(self,request, total=0, quantity=0, cart_items=None):
        try:
            tax=0
            grand_total=0
            cart = Cart.objects.get(cart_id=_card_id(request))
            cart_items = CartItem.objects.filter(cart=cart, is_active=True)
            for cart_item in cart_items:
                total += (cart_item.product.price * cart_item.quantity)
                quantity += cart_item.quantity
            tax = (2 * total)/100
            grand_total = total + tax


        except ObjectDoesNotExist:
            pass

        context = {
            'total' : total,
            'quantity': quantity,
            'cart_items': cart_items,
            'tax'       : tax,
            'grand_total': grand_total,
        } 
        return render(request, self.template_name, context)
