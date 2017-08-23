from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from ..login_app.models import User
from .models import Car

# Create your views here.
def sessionChecker(request):
    try:
        return request.session['user_id']
    except:
        return False

def index(request):
    if sessionChecker(request) == False:
        return redirect('/')

    context = {
        'cars': Car.objects.all(),
        'user': User.objects.get(id = request.session['user_id']),
    }
    return render(request, 'car_app/index.html', context)

def add(request):
    if sessionChecker(request) == False:
        return redirect('/')

    return render(request, 'car_app/add.html')

def submit_car(request):
    results = Car.objects.carVal(request.POST)
    if results['status'] == True:
        for error in results['errors']:
            messages.error(request, error)
        return redirect('/cars/add')
    print results
    return redirect('/cars')

def all(request):
    if sessionChecker(request) == False:
        return redirect('/')

    context = {
        'users': User.objects.all(),
    }
    return render(request, 'car_app/all.html', context)

def own(request, car_id, user_id):
    User.objects.get(id = user_id).cars_owned.add(Car.objects.get(id = car_id))
    return redirect('/cars')

def unown(request, car_id, user_id):
    User.objects.get(id = user_id).cars_owned.remove(Car.objects.get(id = car_id))
    return redirect('/cars')

def show(request, user_id):
    if sessionChecker(request) == False:
        return redirect('/')

    context = {
        'user': User.objects.get(id = user_id),
    }
    return render(request, 'car_app/show.html', context)
