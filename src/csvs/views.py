import csv
from django.shortcuts import render
from .forms import CsvForm
from .models import Csv
from django.contrib.auth.models import User
from products.models import Product, Purchase


def upload_file_view(request):
    error_message = None
    success_message = None
    form = CsvForm(request.POST or None, request.FILES or None)
    print(f'form_1 - {form}')
    if form.is_valid():
        form.save()
        form = CsvForm()
        print(f'form_2 - {form}')

        try:
            print('In try block')
            obj = Csv.objects.get(activated=False)
            print(f'obj - {obj}')
            with open(obj.file_name.path, 'r') as f:
                reader = csv.reader(f)
                print(f'reader - {reader}')

                for row in reader:
                    print(row)
                    print(type(row))

                    # row = ''.join(row)
                    # print(row)
                    # row = row.replace(',', ' ')
                    # print(row)
                    # row = row.split()
                    # print(row)
                    # print(type(row))

                    user = User.objects.get(id=row[3])
                    print(user)
                    prod, _ = Product.objects.get_or_create(name=row[0])
                    print(prod)
                    Purchase.objects.create(
                        product=prod,
                        price=int(row[2]),
                        quantity=int(row[1]),
                        salesman=user,
                        date=row[4]
                    )

            obj.activated = True
            obj.save()
            success_message = 'Uploaded successfully'
            print('Uploaded successfully')
        except:
            error_message = 'Ups. Something went wrong...'
            print('Ups. Something went wrong...')

    context = {
        'form': form,
        'success_message': success_message,
        'error_message': error_message,
    }
    return render(request, 'csvs/upload.html', context)
