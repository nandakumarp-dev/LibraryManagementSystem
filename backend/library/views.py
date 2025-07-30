from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.db.models import Q
from .models import Borrower, Book
from .forms import BorrowerForm
from .forms import BookForm

# --- Borrower Views ---

class BorrowerCreateView(View):
    def get(self, request):
        form = BorrowerForm()
        return render(request, 'library/borrower_form.html', {'form': form})
    
    def post(self, request):
        form = BorrowerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('borrower-list')
        return render(request, 'library/borrower_form.html', {'form': form})


class BorrowerListView(View):
    def get(self, request):
        query = request.GET.get('query')
        borrowers = Borrower.objects.all()
        if query:
            borrowers = borrowers.filter(
                Q(name__icontains=query) | Q(book__title__icontains=query)
            )
        return render(request, 'library/borrower_list.html', {'borrowers': borrowers})



class BorrowerUpdateView(View):
    def get(self, request, pk):
        borrower = get_object_or_404(Borrower, pk=pk)
        form = BorrowerForm(instance=borrower)
        return render(request, 'library/update_borrowed_date.html', {'form': form})
    
    def post(self, request, pk):
        borrower = get_object_or_404(Borrower, pk=pk)
        form = BorrowerForm(request.POST, instance=borrower)
        if form.is_valid():
            form.save()
            return redirect('borrower-list')
        return render(request, 'library/update_borrowed_date.html', {'form': form})


class BorrowerDetailView(View):
    def get(self, request, pk):
        borrower = get_object_or_404(Borrower, pk=pk)
        return render(request, 'library/borrower_detail.html', {'borrower': borrower})


# --- Book Views ---

class BookCreateView(View):
    def get(self, request):
        form = BookForm()
        return render(request, 'library/book_form.html', {'form': form})
    
    def post(self, request):
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book-list')
        return render(request, 'library/book_form.html', {'form': form})


class BookListView(View):
    def get(self, request):
        books = Book.objects.all()
        return render(request, 'library/book_list.html', {'books': books})



class BookUpdateView(View):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        form = BookForm(instance=book)
        return render(request, 'library/book_form.html', {'form': form, 'object': book})
    
    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book-list')
        return render(request, 'library/book_form.html', {'form': form, 'object': book})


class BookDetailView(View):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        return render(request, 'library/book_detail.html', {'book': book})
