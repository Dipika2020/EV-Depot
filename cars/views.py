from datetime import datetime, timedelta
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.http import require_http_methods
# Create your views here.
from cars.models import Cars
from forms import CarForm

def index(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cars:homepage')  # Redirect to the same page to clear the form
    else:
        form = CarForm()

    cars = Cars.objects.all().order_by('-createdAt')
    car_form = CarForm()
    context = {
        'cars': cars,
        'form': car_form
    }
    return render(request,'index.html', context)

def carById(request, id):
    car = get_object_or_404(Cars, id=id)
    return render(request, 'car.html', {'car': car})

def deleteCar(request, id):
    if request.method == 'DELETE':
        print(f"Received DELETE request for car ID {id}")
        car = get_object_or_404(Cars, pk=id)
        car.delete()
        return JsonResponse({"message": "Bike deleted successfully."}, status=200)
    else:
        print(f"Received {request.method} request, only DELETE is allowed")
        raise Http404("Only DELETE method is allowed")