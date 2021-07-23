from django.shortcuts import render
from django.views import View
# Create your views here.
class CartView(View):
    def get(self, request):
        user = request.user
        print(user)
        return render(request, "store/cart.html")

    def post (self, request):
        pass

    def update(self, update):
        pass

    def delete(self, request):
        pass
