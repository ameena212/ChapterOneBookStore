from django.views import generic
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView
from .models import Book
from .forms import BookForm
from django.shortcuts import render

def chapter_one_view(request):
    return render(request, 'chapter_one.html')

def homeView(request):
    return render(request, 'home.html')

class BookDetailView(DetailView):
    model = Book
    template_name = 'book_details.html'

class BookView(ListView):
    model = Book
    template_name = 'sell_books.html'

class AddBookView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'add_sell_books.html'

def sell_books_view(request):
    context = {}
    return render(request, 'sell_books.html', context)
