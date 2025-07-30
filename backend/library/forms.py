from django import forms
from .models import Borrower

class BorrowerForm(forms.ModelForm):
    class Meta:
        model = Borrower
        fields = ['name', 'email', 'book', 'borrowed_date']
        widgets = {
            'borrowed_date': forms.DateInput(attrs={'type': 'date'})
        }