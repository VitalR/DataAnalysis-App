from django.shortcuts import render
from .models import Product, Purchase
from .utils import get_simple_plot
from .forms import PurchaseForm
import pandas as pd


def chart_select_view(request):
    df = None
    graph = None
    error_message = None
    price = None

    product_df = pd.DataFrame(Product.objects.all().values())
    purchase_df = pd.DataFrame(Purchase.objects.all().values())
    # qs1 = Product.objects.all().values()
    # qs2 = Product.objects.all().values_list()
    # print(product_df)
    # print('------')
    # print(qs2)

    product_df['product_id'] = product_df['id']

    # print(purchase_df.shape)
    # print(product_df.shape)

    if purchase_df.shape[0] > 0:  # if there is a data in database
        df = pd.merge(purchase_df, product_df, on='product_id').drop(['id_y', 'date_y'], axis=1).rename(
            {'id_x': 'id', 'date_x': 'date'}, axis=1)
        price = df['price']
        # print(df['date'][0])
        # print(type(df['date'][0]))
        if request.method == 'POST':
            print(request.POST)
            chart_type = request.POST.get('sales')
            date_from = request.POST['date_from']
            date_to = request.POST['date_to']
            # print(chart_type)
            # print(date_from, date_to)

            df['date'] = df['date'].apply(lambda x: x.strftime('%Y-%m-%d'))
            # print(df['date'])
            df2 = df.groupby('date', as_index=False)['total_price'].agg('sum')
            # print(df2)

            if chart_type != '':
                if date_from != '' and date_to != '':
                    df = df[(df['date'] > date_from & df['dare'] < date_to)]
                    df2 = df.groupby('date', as_index=False)['total_price'].agg('sum')
                # function to get a graph
                graph = get_simple_plot(chart_type, x=df2['date'], y=df2['total_price'], data=df)
            else:
                error_message = 'Please select a chart type to continue'
    else:
        error_message = 'No records in the database'

    context = {
        'graph': graph,
        'price': price,
        'error_message': error_message,
        # 'chart_error_message': chart_error_message,
        # 'products': product_df.to_html(),
        # 'purchase': purchase_df.to_html(),
        # 'df': df,
    }
    return render(request, 'products/main.html', context)


def add_purchase_view(request):
    form = PurchaseForm()

    context = {
        'form': form,
    }
    return render(request, 'products/add.html', context)