from django.db import models

class Book(models.Model):

    title = models.CharField(max_length=200)

    author = models.CharField(max_length=100)

    published_date = models.DateField()

    isbn = models.CharField(max_length=13, unique=True)

    def __str__(self):

        return self.title

class Borrower(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField()

    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    borrowed_date = models.DateField()

    def __str__(self):
        
        return self.name