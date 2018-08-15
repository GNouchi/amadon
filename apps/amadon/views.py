from django.shortcuts import render , redirect, HttpResponse
from .models import *
from  django.utils.crypto import get_random_string 

# this is added to db in index method
arr=  [{'price':19.99, 'item': "Dojo Tshirt"},{'price':29.99, 'item': "Dojo Sweater"},{'price':4.99, 'item': "Dojo Cup"},{'price':49.99, 'item': "Algorithm Book"}]

def index(request):
# allowing old cust to become new cust by flushing sessions (different wallets)
    if 'id' not in request.session:                 
        request.session['id'] = get_random_string(length=140)
        request.session['last'] = 0
        request.session['totalspent'] = 0
        request.session['totalitems'] = 0
        print("welcome")
        print("Generated keys: ", request.session.keys())
# loop in all our Prod values, can also remove first if statement to overwrite existing
    if len(Prod.objects.all())==0:
        for i in range(len(arr)):
            if Prod.objects.filter(item = arr[i]['item']).exists()==False:
                Prod.objects.create(item = arr[i]['item'],price = arr[i]['price'] )
                print("ADDED  : ", Prod.objects.last())
                print("NEW LIST" , Prod.objects.all().values())
    context = {'db' : Prod.objects.all()}
    return render(request, 'index.html', context)

def process(request, id):
    x = round(float(Prod.objects.get(id = id).price),2)
    y = int(request.POST['qty'])
    print("checkout total == ",y*x)
    request.session['totalitems'] += y
    request.session['last'] = y*x
    request.session['totalspent'] += request.session['last']
    return redirect('/amadon/checkout')

def checkout(request):
    if 'last' not in request.session:
        print("triger1")
        return redirect('/amadon')
    if request.session['last'] == 0:
        print("triger2")
        return redirect('/amadon')
    # print(request.session.keys())
    context = {
        'session':request.session
    }
    return render(request, 'checkout.html', context)
