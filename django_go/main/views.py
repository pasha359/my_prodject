from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from .forms import NotesForm
from .models import *
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

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
            # pos_form.user = request.user
            # pos_form.user.save()
            pos_form.save()

            return redirect('all_notes')
    data = {'pos_form': pos_form, 'media_url': settings.MEDIA_URL}
    return render(request, 'main/add_notes.html', data)

def show_note(request, note_id):
    notes = get_object_or_404(Notes, id=note_id)
    context = {
        'notes':notes,
        'title': 'детали',
        'cat_selected': notes.id
    }
    return render(request, 'main/singl_post.html', context=context)

@login_required()
def all_notes(request):
    notes = Notes.objects.all()

    paginator = Paginator(notes, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'notes':notes,
        'title': 'все записи',
        'page_obj': page_obj,
    }
    return render(request, 'main/all_notes.html', context=context)

@login_required()
def fine_is_paid(request):
    notes = Notes.objects.filter(property__fine_is_paid='NO')
    context = {
        'notes':notes,
        'title': 'не оплаченные штрафы'
    }
    return render(request, 'main/fine_is_paid.html', context=context)

@login_required()
def taken_by_owner(request):
    notes = Notes.objects.filter(property__taken_by_owner='NO')
    context = {
        'notes':notes,
        'title': 'изъятые авто'
    }
    return render(request, 'main/taken_by_owner.html', context=context)


class Search(ListView):
    template_name = 'main/all_notes.html'
    context_object_name = 'notes'
    paginate_by = 5

    def get_queryset(self):
        return Notes.objects.filter(property__property_name=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context
