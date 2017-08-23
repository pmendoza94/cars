from django.shortcuts import render, HttpResponse, redirect
from .models import User
from django.contrib import messages

# Create your views here.
def index(request):
    #This is clear the db if needed!
    # User.objects.all().delete()
    return render(request, 'login_app/index.html')

def register(request):
    results = User.objects.registerVal(request.POST)
    if results['status'] == True:
        for error in results['errors']:
            messages.error(request, error)
    else:
        messages.success(request, 'User has been created! Please login to continue')
    return redirect('/')

def login(request):
    results = User.objects.loginVal(request.POST)
    if results['status'] == True:
        for error in results['errors']:
            messages.error(request, error)
        return redirect('/')
    else:
        request.session['user_id'] = results['user'].id
        request.session['user_name'] = results['user'].first_name
        return redirect('/cars')

def logout(request):
    request.session.flush()
    return redirect('/')
