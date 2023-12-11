from django.urls import path

from . import views

urlpatterns = [
    # ex: books/
    path("", views.get_all_books_author, name="create and view books"),
    
]
