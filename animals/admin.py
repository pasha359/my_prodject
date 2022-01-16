from django.contrib import admin
from .models import Note,Comments

class NoteAdmin(admin.ModelAdmin):
    list_display = ['title','id','img']
    list_display_links = ['title','id']
    search_fields = ['title','place_of_find']

admin.site.register(Note, NoteAdmin) #обяхаькльно указать вторым параметром


admin.site.register(Comments)
