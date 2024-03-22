from django.shortcuts import render
from .models import MyModel

def home(request):
    return render(request, 'home.html')

def show_all_records(request):
    all_records = MyModel.objects.all()

    records_to_delete = []

    for record in all_records:
        if any(char.isdigit() and int(char) % 2 != 0 for char in record.title):
            records_to_delete.append(record.id)

    MyModel.objects.filter(id__in=records_to_delete).delete()

    all_records = MyModel.objects.all()

    return render(request, 'all_records.html', {'records': all_records})
