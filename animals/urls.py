from . import views
from django.urls import path
from animals.api.views import *
from animals.views import *

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('announcement', AnnouncementViewSet)
urlpatterns = router.urls

urlpatterns = urlpatterns + [
    # path('create_comment', CommentCreate.as_view()),
    path('announcement/<int:pk>/', AnnouncementViewSet.as_view({'get': 'update'})),


    path('', views.home, name= 'home'),
    path('about/', views.about, name= 'about'),
    path('add_note/',AddNote.as_view(), name= 'add_note'),
    path('login/', views.login, name= 'login'),
    path('reristration/', views.reristration, name= 'reristration'),
    # path('post/<slug:post_slug>/', views.show_post, name= 'post'), #раскрывает поле "подробнее на глвной странице"
    path('cat', views.show_cat, name= 'cat'),
    path('dog', views.show_dog, name= 'dog'),
    path('bird', views.show_bird, name= 'bird'),
    path('other', views.show_other, name= 'other'),

    path('all_animals', views.all_animals, name = 'all_animals'),
]