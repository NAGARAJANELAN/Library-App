from rest_framework import generics

from books.models import Book
from books.serializers import BookSerializer


# /books
class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# /books/id
class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "id"


# books/
# class BookList(APIView):
#     """
#     Lists all books and creates new book
#     """
#     def

# @csrf_exempt
# def handle_book_request(request):
#     if request.method == "GET":
#         return get_all_books()
#     elif request.method == "POST":
#         return create_book(request)
#     else:
#         return JsonResponse({"error": "Unsupported method"}, status=405)


# def get_all_books():
#     fetched_books = Book.objects.all()
#     response = ""
#     for book in fetched_books:
#         response += "<h1> {} </h1>".format(book)
#     return HttpResponse(response)


# @csrf_exempt
# def create_book(request):
#     data = request_json_helper(request)
#     name = data["name"]
#     initial_copies = data["initial_copies"]
#     author_ids = data["author_ids"]

#     # creating entry in Book table
#     book = Book.objects.create(name=name, count=initial_copies)

#     # adding authors to book
#     for author_id in author_ids:
#         author = get_author_by_id(author_id)
#         book.authors.add(author)
#         book.save()

#     book.save()
#     return HttpResponse("Book added")


# # books/{id}
# @csrf_exempt
# def handle_book_by_id(request, book_id):
#     print(request.method)
#     if request.method == "DELETE":
#         return delete_book_by_id(book_id)
#     elif request.method == "GET":
#         return get_book_by_id(book_id)
#     elif request.method == "PUT":
#         return update_book_by_id(request, book_id)
#     else:
#         return JsonResponse({"error": "Unsupported method"}, status=405)


# def get_book_by_id(book_id):
#     fetched_book = Book.objects.get(id=book_id)
#     return HttpResponse("<h1> {} </h1>".format(fetched_book))


# @csrf_exempt
# def update_book_by_id(request, book_id):
#     data = request_json_helper(request)

#     name = data["name"]
#     copies_count = data["copies_count"]

#     fetched_book = Book.objects.get(id=book_id)
#     fetched_book.name = name
#     fetched_book.count = copies_count
#     author_ids = data["author_ids"]

#     # handling authors updation for books
#     fetched_book.authors.clear()
#     fetched_book.save()

#     for author_id in author_ids:
#         author = get_author_by_id(author_id)
#         fetched_book.authors.add(author)
#         fetched_book.save()
#     fetched_book.save()

#     return HttpResponse("Book Updated")


# @csrf_exempt
# def delete_book_by_id(book_id):
#     try:
#         fetched_book = Book.objects.get(id=book_id)
#         fetched_book.delete()
#         return HttpResponse("Books Deleted")
#     except:
#         return HttpResponse("Error Deleting Book")


# def request_json_helper(request):
#     raw_data = request.body.decode("utf-8")
#     try:
#         data = json.loads(raw_data)
#         return data
#     except json.JSONDecodeError:
#         return JsonResponse({"error": "Invalid JSON data"}, status=400)
