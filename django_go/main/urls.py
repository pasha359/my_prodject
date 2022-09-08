from main.api.views import *
from django.urls import path
from .views import Search
from rest_framework.routers import DefaultRouter, SimpleRouter
from . import views

router = SimpleRouter()
router.register('api/notes', NoteViewSet)
urlpatterns = router.urls

urlpatterns = urlpatterns + [
    path('/api/notes/<int:pk>/', NoteViewSet.as_view({'get': 'update'})),

    path('', views.home, name= 'home' ),
    path('add_notes/', views.add_notes, name = 'add_notes'),
    path('all_notes/', views.all_notes, name = 'all_notes'),
    path('fine_is_paid/', views.fine_is_paid, name = 'fine_is_paid'),
    path('taken_by_owner/', views.taken_by_owner, name = 'taken_by_owner'),
    path('note/<int:note_id>/', views.show_note, name = 'note'),
    path('search/',Search.as_view(), name='search')



]