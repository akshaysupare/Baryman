import email
from django.shortcuts import render
from testapp.models import User
import datetime

# Create your views here.

def home_view(request):
     return render(request,'testapp/index.html')

def about_view(request):
    return render(request,'testapp/about.html')

def contact_view(request):

    if request.method == 'POST':
        dt = datetime.now()
        email = request.POST.get('email')
        name = request.POST.get('name')
        print('hii man how are your    ')
        print(email)
        print(name)
    return render(request,'testapp/contact.html')
    
def product_view(request):
    return render(request,'testapp/products.html')

def one_view(request):
    return render(request,'testapp/one.html')

def half_view(request):
    return render(request,'testapp/half.html')

