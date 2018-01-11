from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre


def index(request):
    """
    View function for home page of site
    """
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_author = Author.objects.all().count()
    num_genre = Genre.objects.all().count()
    num_python_books = Book.objects.filter(title__contains='Python').count()

    return render(
        request,
        'index.html',
        context={'num_books':num_books, 'num_instances': num_instances,
                 'num_instances_available': num_instances_available, 'num_author': num_author, 'num_genre': num_genre,
                 'num_python_books': num_python_books}
    )