from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserRegister

# Create your views here.
def sign_up_by_html(request):
    users = ['Белуга', 'Осётр', 'Лосось', 'Барабулька']
    info = {}
    if request.method == 'POST':
        # Получаем данные
        username = request.POST.get('username')
        if username in users:
            info["error"] = 'Пользователь уже существует'
            return HttpResponse(info["error"])
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        if password != repeat_password:
            info["error"] = 'Пароли не совпадают'
            return HttpResponse(info["error"])
        age = request.POST.get('age')
        if int(age) < 18:
            info["error"] = 'Вы должны быть старше 18'
            return HttpResponse(info["error"])
        send = request.POST.get('send') == 'on'
        # users.append(username)
        return HttpResponse(f'Приветствуем, {username}!')

    return render(request, 'registration_page.html')



def sign_up_by_django(request):
    users = ['Белуга', 'Осётр', 'Лосось', 'Барабулька']
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            # Обработка данных формы
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            send = form.cleaned_data['send']
    else:
        form = UserRegister()
    return render(request,'registration_page.html', {'form': form})