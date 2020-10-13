import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from django.shortcuts import render
from .models import Customer
from products.utils import get_image


def customer_corr_view(request):
    df = pd.DataFrame(Customer.objects.all().values())
    corr = round(df['budget'].corr(df['employment']), 2)  # correlation

    plt.switch_backend('Agg')
    sns.jointplot(x='budget', y='employment', kind='reg', data=df).set_axis_labels('Company budget',
                                                                                     'No of employees')
    graph = get_image()

    context = {
        'graph': graph,
        'corr': corr,
    }

    return render(request, 'customers/main.html', context)
