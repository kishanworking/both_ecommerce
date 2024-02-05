# for navabr counter showing total product presend 

from .models import Cart, CartItem
from .views import _card_id
def counter(request):
    cart_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = Cart.objects.filter(cart_id=_card_id(request))
            cart_items = CartItem.objects.all().filter(cart=cart[:1])
            for i in cart_items:
                cart_count = cart_count + i.quantity
        except Cart.DoesNotExist:
            cart_count = 0
    return dict(cart_count=cart_count)