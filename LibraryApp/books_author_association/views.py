from django.shortcuts import render
from django.http import HttpResponse
from .models import BooksAuthorAssociation

# Create your views here.
def get_all_books_author(request):
    books_author_associations = BooksAuthorAssociation.objects.all()
    response=''
    for association in books_author_associations:
        response += association.book.book_name+' '+association.author.author_name+'<br>'
    return HttpResponse(response)