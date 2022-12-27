from django.db import models
from django.contrib.auth.models import User

# Create your models here.


everyone = (
    ('Patient', 'Patient'),
    ('Doctor', 'Doctor'),

)


class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    gender=models.CharField(max_length=200, null=True, choices=everyone)


    def __str__(self):
        return self.user.username


class Pharmecy(models.Model):
    name=models.CharField(max_length=20)
    image=models.ImageField(upload_to='permecy',null=True)
    price=models.PositiveIntegerField()
    description=models.TextField(max_length=250)


class Payment(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=20)
    phone=models.PositiveIntegerField()
    address=models.TextField(max_length=300)
    total = models.IntegerField(null=True)

    def __str__(self):
        return self.username
class Specialist(models.Model):
    pic=models.ImageField()
    des=models.TextField(max_length=200)
PROFESSION_CHOICES =(
    ('food','food'),
    ('child','child'),
    ('nurologist','nurologist'),
    ('medicine','medicine'),

)

class DoctorDetails(models.Model):
    picture=models.ImageField(upload_to='special_doctor')
    name=models.CharField(max_length=100)
    desp=models.TextField(max_length=200)
    workplace=models.CharField(max_length=200)
    exprience=models.PositiveIntegerField()
    price=models.PositiveIntegerField()
    profession=models.CharField(max_length=50,choices=PROFESSION_CHOICES,null=True)

    def __str__(self):
        return self.name


class DoctorAppoint(models.Model):
    pic=models.ImageField(upload_to='doc',null=True)
    type=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    hospital_name=models.CharField(max_length=200)
    profession=models.CharField(max_length=200)
    place=models.CharField(max_length=200)
    price=models.PositiveIntegerField()
    designation = models.CharField(max_length=200,null=True)
    specialization_area = models.CharField(max_length=200,null=True)
    department = models.CharField(max_length=200,null=True)
    education = models.TextField(max_length=500,null=True)
    training = models.TextField(max_length=500,null=True)
    research = models.TextField(max_length=500,null=True)

    def __str__(self):
        return self.name

class AvailableAppoint(models.Model):
    name=models.CharField(max_length=200)
    available=models.CharField(max_length=200)
    price=models.PositiveIntegerField(null=True)


class Booking(models.Model):
    time=models.TimeField()
    date=models.DateField()
    name=models.CharField(max_length=200)
    price=models.PositiveIntegerField()
    email=models.EmailField(max_length=30)
    number=models.PositiveIntegerField()

    def __str__(self):
        return self.name
class Confirm(models.Model):
    card=models.PositiveIntegerField()
    expire=models.TextField()
    cvc=models.PositiveIntegerField()
    country=models.CharField(max_length=200)
class Emergency(models.Model):
    name=models.CharField(max_length=200)
    ambulance_number=models.PositiveIntegerField()
    contact=models.PositiveIntegerField()
    place=models.TextField()

    def __str__(self):
        return self.name
class AmbulanceDetails(models.Model):
    img=models.ImageField(upload_to='emergengy')
    name=models.CharField(max_length=200)
    car_number=models.PositiveIntegerField(null=True)
    description=models.TextField()
class Blood(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    address=models.TextField()
    number=models.PositiveIntegerField()
    blood=models.TextField()
    age=models.PositiveIntegerField()

    def __str__(self):
        return self.blood

class Blog(models.Model):
    image=models.ImageField(upload_to='blog')
    pic=models.ImageField(upload_to='blogpic')
    name=models.CharField(max_length=200,null=True)
    title=models.CharField(max_length=200)
    text=models.TextField(null=True)
    description=models.TextField()



