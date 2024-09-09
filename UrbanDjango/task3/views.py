from django.shortcuts import render


# Create your views here.
def home(request):
    title = 'магазин АБЫРВАЛГ'
    page_title = 'Главная страница'
    link1 = 'Главная'
    link2 = 'Магазин'
    link3 = 'Корзина'
    context = {
        'title': title,
        'page_title': page_title,
        'link1': link1,
        'link2': link2,
        'link3': link3,
    }
    return render(request, 'home.html', context)


def store(request):
    title = 'магазин АБЫРВАЛГ'
    page_title = 'Рыбы'
    fish1 = 'Белуга'
    fish2 = 'Осётр'
    fish3 = 'Лосось'
    context = {
        'title': title,
        'page_title': page_title,
        'fish1': fish1,
        'fish2': fish2,
        'fish3': fish3,
    }
    return render(request, 'store.html', context)


def basket(request):
    title = 'магазин АБЫРВАЛГ'
    context = {
        'title': title,
    }
    return render(request, 'basket.html', context)
