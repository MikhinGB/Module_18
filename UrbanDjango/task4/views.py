from django.shortcuts import render

# Create your views here.
def home(request):
    title = 'магазин АБЫРВАЛГ'
    page_title = 'Главная страница'
    link1 = 'Главная'
    link2 = 'Магазин'
    link3 = 'Садок'
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
    link1 = 'Главная'
    link2 = 'Магазин'
    link3 = 'Садок'
    fish = ['Белуга', 'Осётр', 'Лосось', 'Барабулька']
    context = {
        'title': title,
        'page_title': page_title,
        'fish': fish,
        'link1': link1,
        'link2': link2,
        'link3': link3,
    }
    return render(request, 'store.html', context)


def basket(request):
    title = 'магазин АБЫРВАЛГ'
    page_title = 'Садок'
    link1 = 'Главная'
    link2 = 'Магазин'
    link3 = 'Садок'
    context = {
        'title': title,
        'page_title': page_title,
        'link1': link1,
        'link2': link2,
        'link3': link3,
    }
    return render(request, 'basket.html', context)

