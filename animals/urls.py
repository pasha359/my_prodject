from . import views
from django.urls import path
from animals.api.views import NoteCreate, CommentsCreate, ListNoteView, NoteDetailView,ListCommentsView


urlpatterns = (
    path('create_note', NoteCreate.as_view()),
    path('create_comment', CommentsCreate.as_view()),

    path('all_coments', ListCommentsView.as_view()),
    path('all/', ListNoteView.as_view()),
    path('all/<int:pk>/', NoteDetailView.as_view()),

    path('', views.home, name= 'home'),
    path('about/', views.about, name= 'about'),
    path('add_note/', views.add_note, name= 'add_note'),
    path('login/', views.login, name= 'login'),
    path('reristration/', views.reristration, name= 'reristration'),
    path('post/<int:post_id>/', views.show_post, name= 'post'), #раскрывает поле "подробнее на глвной странице"
    path('add_note/', views.add_note, name = 'add_page')
)