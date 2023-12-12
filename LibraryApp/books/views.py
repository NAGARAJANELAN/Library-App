import json
from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Book

from authors.models import Author
from authors.helper import get_author_by_id
from books_author_association.models import BooksAuthorAssociation
from books_author_association.helper import create_book_author_association

# books/
@csrf_exempt
def handle_book_request(request):
    if request.method == "GET":
        return get_all_books()
    elif request.method == "POST":
        return create_book(request)
    else:
        return JsonResponse({"error": "Unsupported method"}, status=405)


def get_all_books():
    fetched_books = Book.objects.all()
    response = ""
    for book in fetched_books:
        response += "<h1> {} </h1>".format(book)
    return HttpResponse(response)


@csrf_exempt
def create_book(request):
    data = request_json_helper(request)
    name = data["name"]
    initial_copies = data["initial_copies"]

    # creating entry in Book table
    book = Book(book_name=name, copies_count=initial_copies)
    book.save()
    
    # create entry in BooksAuthorAssociation
    author_ids=data["author_ids"]
    for author_id in author_ids:
        author=get_author_by_id(author_id)
        create_book_author_association(book,author)
        
    return HttpResponse("Book added")


# books/{id}
@csrf_exempt
def handle_book_by_id(request, book_id):
    print(request.method)
    if request.method == "DELETE":
        return delete_book_by_id(book_id)
    elif request.method == "GET":
        return get_book_by_id(book_id)
    elif request.method == "PUT":
        return update_book_by_id(request, book_id)
    else:
        return JsonResponse({"error": "Unsupported method"}, status=405)


def get_book_by_id(book_id):
    fetched_book = Book.objects.get(book_id=book_id)
    return HttpResponse("<h1> {} </h1>".format(fetched_book))


@csrf_exempt
def update_book_by_id(request, book_id):
    data = request_json_helper(request)

    name = data["name"]
    copies_count = data["copies_count"]

    fetched_book = Book.objects.get(book_id=book_id)
    fetched_book.book_name = name
    fetched_book.copies_count = copies_count
    
    # handling authors updation for books
    associations=BooksAuthorAssociation.objects.filter(book=fetched_book)
    associations.delete()
    
    author_ids=data["author_ids"]
    for author_id in author_ids:
        author=get_author_by_id(author_id)
        create_book_author_association(fetched_book,author)
        
    fetched_book.save()
    return HttpResponse("Book Updated")


@csrf_exempt
def delete_book_by_id(book_id):
    try:
        fetched_book = Book.objects.get(book_id=book_id)
        associations=BooksAuthorAssociation.objects.filter(book=fetched_book)
        for association in associations:
            association.author.book_count-=1
            association.author.save()
        fetched_book.delete()
        return HttpResponse("Books Deleted")
    except:
        return HttpResponse("Error Deleting Book")


def request_json_helper(request):
    raw_data = request.body.decode("utf-8")
    try:
        data = json.loads(raw_data)
        return data
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON data"}, status=400)
