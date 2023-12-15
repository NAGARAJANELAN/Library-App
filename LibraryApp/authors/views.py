from rest_framework import generics

from authors.models import Author
from authors.serializers import AuthorSerializer


# /authors
class AuthorList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


# /authors/id
class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    lookup_field = "id"


# Does same as above
#
# class AuthorList(APIView):
#     """
#     Lists all authors and creates new author
#     """

#     def get(self, request):
#         authors_fetched = Author.objects.all()
#         serializer = AuthorSerializer(authors_fetched, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     def post(self, request):
#         serializer = AuthorSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, safe=False)
#         return JsonResponse(
#             {"creation": "failure", "errors": serializer.errors},
#             status=status.HTTP_400_BAD_REQUEST,
#         )


# # authors/{id}
# class AuthorDetail(APIView):
#     """
#     Retrieve , update and delete author instance
#     """

#     def get_author(self, id):
#         try:
#             return Author.objects.get(id=id)
#         except Author.DoesNotExist:
#             raise Http404

#     def get(self, request, id):
#         author = self.get_author(id)
#         serializer = AuthorSerializer(author)
#         return JsonResponse(serializer.data, safe=False)

#     def put(self, request, id):
#         author = self.get_author(id)
#         serializer = AuthorSerializer(author, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, safe=False)
#         return JsonResponse(
#             {"updation": "failure", "errors": serializer.errors},
#             status=status.HTTP_400_BAD_REQUEST,
#         )

#     def delete(self, request, id):
#         author = self.get_author(id)
#         author.delete()
#         return JsonResponse({"deletion": "success"}, status=status.HTTP_400_BAD_REQUEST)
