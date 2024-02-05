from django.http import HttpResponse
from django.shortcuts import render
from store_app.models import Product

from django.views.generic import View

class Home(View):
    template_name = "home.html"
    
    def get(self,request):
        product = Product.objects.all().filter(is_available=True)
        context = {
        'products': product,
        }
        return render(request, self.template_name , context)

