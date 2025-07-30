from django import forms
from .models import Borrower
from .models import Book

class BorrowerForm(forms.ModelForm):

    class Meta:

        model = Borrower

        fields = ['name', 'email', 'book', 'borrowed_date']

        widgets = {
            'borrowed_date': forms.DateInput(attrs={'type': 'date'})
        }

class BookForm(forms.ModelForm):

    class Meta:

        model = Book
        
        fields = ['title', 'author', 'published_date', 'isbn']