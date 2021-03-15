import csv, io
from django.http import Http404
from django.shortcuts import render
from django.contrib import messages
from .models import Factory, Car, Dealership, Client


def indexView(request):
    return render(request, 'index.html')


def factoryView(request):
    """ Display all the factories in the database ordered by name"""
    all_factories_to_display = Factory.objects.order_by('name')
    context = {'all_factories': all_factories_to_display}
    return render(request, 'factory/factory_list.html', context)


def factoryDetailView(request, factory_id):
    """ Detailed view of the factories production"""
    try:
        factory_detail_view = Factory.objects.get(pk=factory_id)
    except Factory.DoesNotExist:
        raise Http404("Does not exist")
    return render(request, 'factory/factory_detail.html', {'factory': factory_detail_view})


def dealershipView(request):
    all_dealership_to_display = Dealership.objects.all()
    context = {'all_dealership': all_dealership_to_display}
    return render(request, 'dealership/dealership_list.html', context)


def dealershipDetailView(request, dealership_id):
    try:
        dealership_detail_view = Dealership.objects.get(pk=dealership_id)
    except Dealership.DoesNotExist:
        raise Http404("Does not exist")
    return render(request, 'dealership/dealership_detail.html',
                  {'dealership': dealership_detail_view})


def upload_view(request):
    """ View function that allows uploading csv files and import the data to the database (sqlite)"""
    if request.method == 'GET':
        return render(request, 'upload.html')

    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not csv file')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Car.objects.update_or_create(
            model=column[0],
            type=column[1],
            color=column[2],
            derivative=column[3],
            produced=column[4],
            vin=column[5],
            currently_available=column[6],
            car_owner_id=column[7],
        )

    context = {}
    return render(request, 'upload.html', context)
