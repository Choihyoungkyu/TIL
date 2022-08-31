from django.shortcuts import render
import random

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')

def greeting(request):
    names = ['Eunkyung', 'Hyoungkyu']
    info = {
        'name': 'Hyoungkyu',
        'sur_name': 'Choi'
    }
    context = {
        'names': names,
        'info' : info,
    }
    return render(request, 'articles/greeting.html', context)

def dinner(request):
    foods = ['파스타', '스테이크', '스시', '불고기']
    pick = random.choice(foods)
    context = {
        'pick':pick,
        'foods':foods,
    }
    return render(request, 'articles/dinner.html', context)

def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    message = request.GET.get('message')
    print("message=",message)
    context = {
        'message': message,
    }
    return render(request, 'articles/catch.html', context)

def hello(request, name):
    context = {
        'name' : name,
    }
    return render(request, 'articles/hello.html', context)

def num(request, num):
    context = {
        'num' : num,
    }
    return render(request, 'articles/num.html', context)