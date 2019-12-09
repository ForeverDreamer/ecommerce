from django.http import HttpResponse


def cart_home(request):
    cart_id = request.session.get('cart_id', None)
    if cart_id is None:
        print('create new cart')
        request.session['cart_id'] = 1
    key = request.session.session_key

    request.session['username'] = request.user.username
    result = 'key: {} -- cart_id: {} -- username: {}'.format(key, request.session.get('cart_id'),
                                                             request.session.get('username'))
    return HttpResponse(result)
