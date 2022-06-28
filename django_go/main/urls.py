from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name= 'home' ),
    path('add_notes/', views.add_notes, name = 'add_notes'),
    path('all_notes/', views.all_notes, name = 'all_notes'),
    path('fine_is_paid/', views.fine_is_paid, name = 'fine_is_paid'),
    path('taken_by_owner/', views.taken_by_owner, name = 'taken_by_owner'),



]