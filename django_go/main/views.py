from django.shortcuts import render, redirect

import users.models
from .forms import NotesForm
from .models import *
from django.conf import settings
from django.contrib.auth.decorators import login_required


def home (request):
    context = {
        'title': 'Главная страница',
    }
    return render(request, 'main/about.html', context=context)

@login_required()
def add_notes(request):
    pos_form = NotesForm()
    if request.method == 'POST':
        pos_form = NotesForm(request.POST, request.FILES)
        if pos_form.is_valid():
            pos_form.user = request.user
            pos_form.user.save()
            pos_form.save()

            return redirect('all_notes')
    data = {'pos_form': pos_form, 'media_url': settings.MEDIA_URL}
    return render(request, 'main/add_notes.html', data)

@login_required()
def all_notes(request):
    notes = Notes.objects.all()
    context = {
        'notes':notes,
    }
    return render(request, 'main/all_notes.html', context=context)

@login_required()
def fine_is_paid(request):
    notes = Notes.objects.filter(property__fine_is_paid='NO')
    context = {
        'notes':notes,
    }
    return render(request, 'main/fine_is_paid.html', context=context)

@login_required()
def taken_by_owner(request):
    notes = Notes.objects.filter(property__taken_by_owner='NO')
    context = {
        'notes':notes,
    }
    return render(request, 'main/taken_by_owner.html', context=context)