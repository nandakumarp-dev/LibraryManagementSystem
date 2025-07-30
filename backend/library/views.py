from django.views.generic import CreateView, ListView, UpdateView, DetailView
from django.urls import reverse_lazy
from .models import Borrower
from .forms import BorrowerForm

class BorrowerCreateView(CreateView):
    model = Borrower
    form_class = BorrowerForm
    template_name = 'library/borrower_form.html'
    success_url = reverse_lazy('borrower-list')


class BorrowerListView(ListView):
    model = Borrower
    template_name = 'library/borrower_list.html'
    context_object_name = 'borrowers'


class BorrowerUpdateView(UpdateView):
    model = Borrower
    form_class = BorrowerForm
    template_name = 'library/update_borrowed_date.html'
    success_url = reverse_lazy('borrower-list')


class BorrowerDetailView(DetailView):
    model = Borrower
    template_name = 'library/borrower_detail.html'
    context_object_name = 'borrower'




from .models import Book

from django.views.generic import CreateView, ListView, UpdateView, DetailView
from django.urls import reverse_lazy

# BOOK VIEWS
class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'author', 'published_date', 'isbn']
    template_name = 'library/book_form.html'
    success_url = reverse_lazy('book-list')


class BookListView(ListView):
    model = Book
    template_name = 'library/book_list.html'
    context_object_name = 'books'


class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'author', 'published_date', 'isbn']
    template_name = 'library/book_form.html'
    success_url = reverse_lazy('book-list')


class BookDetailView(DetailView):
    model = Book
    template_name = 'library/book_detail.html'
    context_object_name = 'book'
