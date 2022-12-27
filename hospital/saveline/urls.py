from django.contrib import admin
from django.urls import path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('base',views.base,name='base'),
    path('',views.Home,name='home'),
    path('registration/',views.Registration,name='Registration'),
    path('login/',views.Login,name='login'),
    path('logout/',views.Logout,name='logout'),
    path('patient/',views.Patient,name='patient'),
    path('doctor/',views.Doctor,name='doctor'),
    path('adminpage/',views.Admin,name='admin'),
    # medicine
    path('permecy/',views.Permecy,name='permecy'),
    path('payment/<pk>',views.payments,name='payment'),
    ##specialist
    path('specialisty/',views.Specialisty,name='specialisty'),
    path('food/',views.Food,name='food'),
    path('edit/<str:pk>',views.Edit,name='edit'),
    path('delete/<str:pk>',views.Delete,name='delete'),
    ###appoinment
    path('docappoint/',views.DocAppoint,name='docappoint'),
    path('details/<str:pk>',views.Bookappoint,name='details'),
    path('appointment/',views.Appointment,name='appointment'),
    path('booking/<str:pk>',views.booking,name='booking'),
    path('bookpayment/',views.BookPayment,name='bookpayment'),
    path('confirm/',views.confirms,name='confirm'),
    path('sucessfull/',views.sucessfull,name='sucessfull'),
    path('myappointment/',views.Myappointment,name='myappointment'),
    path('doctorvisit/',views.doctorVisit,name='doctorvisit'),

    ###Ambulance
    path('ambulance/',views.ambulance,name='ambulance'),
    path('ambulanceBooking/',views.ambulanceBooking,name='ambulanceBooking'),

    ###BloodBank
    path('blood/',views.blood,name='blood'),
    path('group/',views.gruoplist,name='group'),

    ###Blog
    path('blog/',views.blog,name='blog'),
    path('blogdetails/<str:pk>',views.blogdetails,name='blogdetails'),
    path('addblog/',views.addBlog,name='addblog'),





]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
