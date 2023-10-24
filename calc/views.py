from django.shortcuts import render,redirect
# Create your views here.
from.models import *

from .forms import OrderForm
def home(request):
    return render(request,'home.html',{'name':'Karthik'})
def add(request):
 val1=int(request.POST['num1'])
 val2=int(request.POST['num2'])
 res=val1+val2
 return render(request,'result.html',{'result':res})

def dashboard(request):
    customers=Customer.objects.all()
    return render(request,'dashboard.html',{'customers':customers})

def products(request):
 products=Product.objects.all()
 return render(request,'products.html',{'prodlist':products})

def customer(request,pk_test):
   customer=Customer.objects.get(id=pk_test)
   customers=Customer.objects.all()
   orders=customer.order_set.all()
   order_count=orders.count()
   context={'customers':customers,'cust':customer, 'ord':orders, 'ord_count':order_count}
   return render(request,'customer.html',context)

def createOrder(request):
   form=OrderForm()

   if request.method=="POST":
      if form.is_valid():
         form.save()
         return redirect('/')
      context={'form':form}
   
   return render(request,'order_form.html',context)
