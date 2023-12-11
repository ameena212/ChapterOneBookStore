from .views import get_cart_info

def cart_info(request):
    cart_total, _ = get_cart_info(request)
    return {'cart_total': cart_total}