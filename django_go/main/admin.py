from django.contrib import admin
from .models import *

class NotesAdmin(admin.ModelAdmin):
    list_display = ['id', 'property','date','contact','user']
    list_display_links = ['id', 'property','date','contact','user']
    search_fields = ['id', 'property','date','contact','user']

class PersonAdmin(admin.ModelAdmin):
    list_display = ['id', 'person_name','age','sex']
    list_display_links = ['id', 'person_name','age','sex']
    search_fields = ['id', 'person_name','age','sex']

class PassportAdmin(admin.ModelAdmin):
    list_display = ['id', 'number', 'person_id']
    list_display_links = ['id', 'number','person_id']
    search_fields = ['id', 'number','person_id']

class PropertyAdmin(admin.ModelAdmin):
    list_display = ['id', 'property_name', 'image', 'fine_is_paid', 'taken_by_owner', 'person_id']
    list_display_links = ['id', 'property_name', 'image', 'fine_is_paid', 'taken_by_owner', 'person_id']
    search_fields = ['id', 'property_name', 'image', 'fine_is_paid', 'taken_by_owner', 'person_id']

admin.site.register(Notes, NotesAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Passport, PassportAdmin)
admin.site.register(Propertys,PropertyAdmin)



