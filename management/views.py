from django.http import Http404
from django.shortcuts import render
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
