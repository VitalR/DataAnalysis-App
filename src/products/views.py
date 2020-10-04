from django.shortcuts import render
from .models import Product, Purchase
import pandas as pd
# Create your views here.

def chart_select_view(request):
    product_df = pd.DataFrame(Product.objects.all().values())
    purchase_df = pd.DataFrame(Purchase.objects.all().values())
    # qs1 = Product.objects.all().values()
    # qs2 = Product.objects.all().values_list()
    print(product_df)
    # print('------')
    # print(qs2)

    context = {
        'products': product_df.to_html(),
        'purchase': purchase_df.to_html(),
    }
    return render(request, 'products/main.html', context)