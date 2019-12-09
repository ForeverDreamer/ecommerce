# from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.reverse import reverse as api_reverse
from rest_framework.views import APIView

from product.models import Product, Category


class APIHomeView(APIView):
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        data = {
            # "auth": {
            #     "login_url": api_reverse("auth_login_api", request=request),
            #     "refresh_url": api_reverse("refresh_token_api", request=request),
            #     "user_checkout": api_reverse("user_checkout_api", request=request),
            # },
            # "address": {
            #     "url": api_reverse("user_address_list_api", request=request),
            #     "create": api_reverse("user_address_create_api", request=request),
            # },
            # "checkout": {
            #     "cart": api_reverse("cart_api", request=request),
            #     "checkout": api_reverse("checkout_api", request=request),
            #     "finalize": api_reverse("checkout_finalize_api", request=request),
            # },
            "product": {
                "count": Product.objects.all().count(),
                "url": api_reverse("product:list", request=request)
            },
            "category": {
                "count": Category.objects.all().count(),
                "url": api_reverse("product:category-list", request=request)
            },
            # "orders": {
            #     "url": api_reverse("orders_api", request=request),
            # }
        }
        return Response(data)


# def home(request):
#     key = request.session.session_key
#     result = 'key: {} -- name: {}'.format(key, request.session.get('name'))
#     return HttpResponse(result)
