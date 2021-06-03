from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Done


def home(request):
    return render(request,'home.html')
def register(request):
    return render(request,'register.html')
def success(request):
    name = request.POST['name']
    username = request.POST['username']
    password = request.POST['password']
    age = request.POST['age']
    number = request.POST['number']
    data = User(name=name, username=username, password=password, age=age, number=number)
    data.save()
    return render(request, 'success.html')

def task(request):
    username2 = request.POST['l_username']
    password2 = request.POST['l_password']
    if User.objects.filter(username=username2, password=password2):
        return render(request, 'index.html')
    else:
        return render(request, 'error.html')

def login(request):
    return render(request,'login.html')
def index(request):
    return render(request,'index.html')

def add(request):
    return render(request,'add.html')
def saved(request):
    name = request.POST['name']
    address = request.POST['address']
    group = request.POST['group']
    contact = request.POST['contact']
    district = request.POST['district']
    age = request.POST['age']
    height = request.POST['height']
    weight = request.POST['weight']
    photo = request.FILES['photo']
    data = Done(name=name, address=address, contact=contact, district=district, age=age, height=height, weight=weight, photo=photo, group=group)
    data.save()
    return render(request, 'saved.html')

def show(request):
    data = Done.objects.all()
    return render(request, 'show.html', {'data': data})

def search(request):
    return render(request,'search.html')

def result(request):
    s = request.GET['search']
    data = Done.objects.filter(group=s)
    return render(request,'result.html',{'data':data})