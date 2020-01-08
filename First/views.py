from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.core.cache import cache

# Create your views here.
def home(request):
    return render(request,'home.html')


def add(request):
    #cache.clear()
    if request.method == 'GET':
        uname = request.GET['uname']
        lname = request.GET['lname']

        request.session['uname'] = uname

        return redirect('/welcome')

        #return render(request,'welcome.html',{'uname':fname})
    else:
        return render(request,'home.html')

def welcome(request):
    cache.clear()
    if request.session.get('uname'):
        return render(request,'welcome.html',{'uname':request.session['uname']})
    else:
        return redirect('home')

def logout(request):
    if request.session.get('uname'):
        try:
            del request.session['uname']
        except KeyError:
            pass
    else:
        pass    
    return redirect('home')