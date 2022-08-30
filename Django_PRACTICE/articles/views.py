from email import message
from multiprocessing import context
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')


def greeting(request):
    foods = ['apple', 'pizza', 'burger']
    five_foods = [food for food in foods if len(food) > 5]
    context = {
        'name': 'KIM KYONGAH',
        'foods': foods,
        'six_foods': five_foods,
    }
    return render(request, 'greeting.html', context)
    # 첫번째 인자는 무조건 request로 고정


def throw(request):
    return render(request, 'throw.html')


def catch(request):
    # print(request)
    # print(type(request))
    # print(request.GET.get('message'))
    department = request.GET.get('department')
    name = request.GET.get('name')

    if department == '대전 2반':
        if name == '김영주':
            message = '교수님이시군요!'
        else:
            message = '교육생이시군요!'
    else:
        message = '다른 반이시군요!'

    context = {
        'message': message
        # 'message': request.GET.get('message')
    }

    return render(request, 'catch.html', context)


def show(request, name):
    context = {
        'name': name,
    }
    return render(request, 'show.html', context)
