from django.urls import path
from .views import BookView
from .views import BookDetailView
from .views import AddBookView
from .views import chapter_one_view
from .views import homeView

from .views import sell_books_view

from . import views 

urlpatterns = [
    path('sell_books',BookView.as_view(), name = "sell_books"),
    path('books/<int:pk>', BookDetailView.as_view(), name="book-details"),
    path('add_sell_books/', AddBookView.as_view(), name="add_sell_books"),
    path('chapter_one/', chapter_one_view, name='chapter_one'),
    path('', homeView, name='home'),
]

