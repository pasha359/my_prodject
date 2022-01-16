from django.shortcuts import render,redirect, HttpResponse
from .models import *
from .forms import AddPostNote
from django.conf import settings


menu = [{'title':'о проекте','url_name':'about'},
        {'title':'опубликовать новость', 'url_name': 'add_note'},
         {'title':'войти', 'url_name': 'login'},
          {'title':'регистрация', 'url_name':'reristration'}
        ]

category = (
    ('кошки','КОШКИ'),
    ('собаки', 'СОБАКИ'),
    ('птицы','ПТИЦЫ'),
    ('земноводные','ЗЕМНОВОДНЫЕ'),
    ('иное','ИНОЕ'),
)

def home(request):
    posts = Note.objects.order_by('-data')
    context = {
        'menu':menu,
        'posts':posts,
        'title': 'Главная страница'
    }
    return render(request, 'animals/home.html', context=context)

def about(request):
    return render(request, 'animals/about.html', {'menu':menu, 'title': 'Главная страница'})


def add_note(request):
    imgs=Note.objects.all()
    error =''
    if request.method == 'POST':
        form = AddPostNote(request.POST, request.FILES)
        if form.is_valid():
            add_note = form.save(commit=False)
            add_note.user = request.user
            add_note.save()
            return redirect('home')
        else:
            error = 'error form'

    form = AddPostNote()
    data ={'form':form, 'menu':menu, 'title':'Добавить заметку','error':error,'img':imgs,'media_url':settings.MEDIA_URL}
    return render(request, 'animals/addpost.html', data)

def login(request):
    return HttpResponse ('Вход')
def reristration(request):
    return HttpResponse ('Регистрация')

def show_post(request, post_id):
    return HttpResponse (f'заметка id {post_id}')