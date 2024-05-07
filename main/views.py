from django.shortcuts import render, redirect

from main.models import Category, Dish, Review, Order


def index(request):
    dishes = Dish.objects.all().order_by('-price')[:4]
    reviews = Review.objects.all()

    context = {
        'dishes': dishes,
        'reviews': reviews,
    }

    return render(request, 'main/index.html', context)


def menu(request):
    categories = Category.objects.all()
    dishes = Dish.objects.all()

    context = {
        'categories': categories,
        'dishes': dishes,
    }

    return render(request, 'main/menu.html', context)


def order_table(request):
    data = request.POST

    if not data['date'] or not data['time']:
        return redirect('index')

    if data:
        order = Order(
            name=data['name'],
            phone=data['phone'],
            date=data['date'],
            time=data['time'],
            people_count=data['count'],
            floor=data['floor'],
        )

        order.save()

    return redirect('index')


def about(request):
    return render(request, 'main/about.html')


def contact(request):
    return render(request, 'main/contact.html')
