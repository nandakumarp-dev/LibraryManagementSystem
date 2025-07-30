from django.urls import path
from .views import (
    BorrowerCreateView, BorrowerListView, BorrowerUpdateView, BorrowerDetailView,BookListView,BookDetailView,BookCreateView,BookUpdateView
)


urlpatterns = [
    path('', BorrowerListView.as_view(), name='borrower-list'),
    path('borrower/add/', BorrowerCreateView.as_view(), name='borrower-add'),
    path('borrower/<int:pk>/', BorrowerDetailView.as_view(), name='borrower-detail'),
    path('borrower/<int:pk>/update/', BorrowerUpdateView.as_view(), name='borrower-update'),
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/add/', BookCreateView.as_view(), name='book-add'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
]