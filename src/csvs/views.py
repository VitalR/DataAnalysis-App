from django.shortcuts import render
from .forms import CsvForm
from .models import Csv
import csv
from django.contrib.auth.models import User


def upload_file_view(request):
    form = CsvForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = CsvForm()

        obj = Csv.objects.get(activated=False)
        with open(obj.file_name.path, 'r') as f:
            reader = csv.reader(f)

            for row in reader:
                print(row)
                print(type(row))
                # row = ''.join(row)
                # print(row)
                # row = row.replace(',', ' ')
                # print (row)
                # row = row.split()
                # print(row)
                # print(type(row))
                user = User.objects.get(id=row[3])
                print(user)

        obj.activated = True
        obj.save()

    context = {
        'form': form,
    }
    return render(request, 'csvs/upload.html', context)
