from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import os


# Create your views here.
def base(request):
    return render(request, 'login/base.html')


def Registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        usr = User.objects.create_user(username, email, password)
        usr.save()
        prod_obj = Customer.objects.create(user=usr, gender=gender)
        prod_obj.save()
    return render(request, 'login/registrtion.html')


def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        gender = request.POST['gender']
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None and user.is_staff==True:
            login(request, user)
            return redirect('doctor')
        else:
            login(request, user)
            return redirect('patient')
    return render(request, 'login/login.html')


def Logout(request):
    logout(request)
    return redirect('login')


def Patient(request):
    medicine = Pharmecy.objects.all()
    special = Specialist.objects.all()
    doctor = DoctorAppoint.objects.all()
    emergency = AmbulanceDetails.objects.all()
    return render(request, 'savelife/patient.html', locals())


def Doctor(request):

    medicine = Pharmecy.objects.all()
    special = Specialist.objects.all()
    doctor = DoctorAppoint.objects.all()
    emergency = AmbulanceDetails.objects.all()
    return render(request, 'savelife/doctor.html',locals())


def Admin(request):
    return render(request, 'savelife/admin.html')
##medicine

def Permecy(request):
    medicine = Pharmecy.objects.all()
    return render(request, 'medicine/permecy.html', locals())


def Home(request):
    medicine = Pharmecy.objects.all()
    special = Specialist.objects.all()
    doctor = DoctorAppoint.objects.all()
    emergency = AmbulanceDetails.objects.all()

    return render(request, 'login/home.html', locals())


def payments(request, pk):
    product = Pharmecy.objects.get(pk=pk)
    shipping_amount = 15
    total = product.price + shipping_amount
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('number')
        address = request.POST.get('address')
        obj = Payment(username=username, email=email, phone=phone, address=address,total=total)
        messages.success(request,'payment successfully')
        obj.save()


    return render(request, 'medicine/payment.html', locals())

###specialist
def Specialisty(request):
    special = Specialist.objects.all()
    return render(request, 'specialist/specialist.html', locals())


def Food(request):
    # specialdoctor = DoctorDetails.filter('food')
    specialdoctor =DoctorDetails .objects.filter(profession='food')

    return render(request, 'specialist/foodspeciality.html', locals())


def Edit(request, pk):
    edit = DoctorDetails.objects.get(id=pk)
    if request.method == 'POST':
        if len(request.FILES) != 0:
            if len(edit.picture) > 0:
                os.remove(edit.picture.path)
            edit.picture = request.FILES['picture']
        edit.name = request.POST.get('name')
        edit.desp = request.POST.get('desp')
        edit.workplace = request.POST.get('workplace')
        edit.exprience = request.POST.get('exprience')
        edit.price = request.POST.get('price')
        edit.save()
        messages.success(request, 'information update successfully')
        return redirect('food')
    return render(request, 'specialist/edit profile.html', locals())


def Delete(request, pk):
    edit = DoctorDetails.objects.filter(id=pk)
    edit.delete()
    messages.success(request, 'delete successfully')
    return redirect('food')


####Appointment
def DocAppoint(request):
    doctor = DoctorAppoint.objects.all()
    return render(request, 'appoinment/docappoint.html', locals())


def Bookappoint(request, pk):
    detail = DoctorAppoint.objects.get(pk=pk)
    return render(request, 'appoinment/details.html', locals())


def Appointment(request):
    appoint = AvailableAppoint.objects.all()
    return render(request, 'appoinment/appointment.html', locals())


def booking(request, pk):
    book = AvailableAppoint.objects.get(pk=pk)
    if request.POST:
        # print('time', request.POST['time'])
        # print('date', request.POST['date'])
        # print('name', request.POST['name'])
        # print('price', request.POST['price'])
        # print('email', request.POST['email'])
        # print('number', request.POST['number'])
        Booking.objects.create(
            time=request.POST['time'],
            date=request.POST['date'],
            name=request.POST['name'],
            price=request.POST['price'],
            email=request.POST['email'],
            number=request.POST['number'],
        )
        return redirect('bookpayment')
    return render(request, 'appoinment/booking.html', locals())


def BookPayment(request):
    data = Booking.objects.all()
    return render(request, 'appoinment/payment.html', locals())


def confirms(request):
    if request.method == 'POST':
        card = request.POST.get('card')
        expire = request.POST.get('expire')
        cvc = request.POST.get('cvc')
        country = request.POST.get('country')
        obj = Confirm(card=card, expire=expire, cvc=cvc, country=country)
        messages.success(request, 'payment successfully')
        obj.save()
        return redirect('sucessfull')

    return render(request, 'appoinment/confirm.html')

def Myappointment(request):
    myappoint=Booking.objects.all()
    return render(request,'appoinment/myappointment.html',locals())

def doctorVisit(request):
    visit = Booking.objects.all()
    return render(request, 'appoinment/visit patient.html', locals())



def sucessfull(request):
    return render(request, 'appoinment/succesfull.html')


####Ambulance
def ambulance(request):
    emergency = AmbulanceDetails.objects.all()
    return render(request, 'ambulance/ambulance.html', locals())


def ambulanceBooking(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        ambulance_number = request.POST.get('ambulance_number')
        contact = request.POST.get('contact')
        place = request.POST.get('place')
        obj = Emergency(name=name, ambulance_number=ambulance_number, contact=contact, place=place)
        messages.success(request, 'Booking successfully')
        obj.save()
    return render(request, 'ambulance/ambulancebooking.html')


####Blood Bank
def blood(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        number = request.POST.get('number')
        blood = request.POST.get('blood')
        age = request.POST.get('age')

        obj = Blood(name=name, email=email, address=address, number=number, blood=blood, age=age)
        obj.save()
        return redirect('group')

    return render(request, 'blood bank/Donate blood.html')


def gruoplist(request):
    group = Blood.objects.all()
    return render(request, 'blood bank/gruoplist.html', locals())


#####Blog
def blog(request):
    blogpage=Blog.objects.all()
    return render(request,'blog/blogpage.html',locals())

def blogdetails(request,pk):
    detail=Blog.objects.get(pk=pk)
    return render(request,'blog/blogdetails.html',locals())
def addBlog(request):
    if request.method =='POST':
        blog=Blog()
        blog.name=request.POST.get('name')
        blog.title = request.POST.get('title')
        blog.text = request.POST.get('text')
        blog.description = request.POST.get('description')
        if len(request.FILES)!=0:
            blog.image=request.FILES['image']
        if len(request.FILES) != 0:
            blog.pic = request.FILES['pic']
        blog.save()
        return redirect('blog')

    return render(request,'blog/addblog.html')
