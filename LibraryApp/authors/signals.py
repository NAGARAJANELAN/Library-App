from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from authors.models import Author

author_list = set()


@receiver(m2m_changed, sender=Author.books_authored.through)
def author_book_count_changed(sender, instance, action, reverse, **kwargs):
    if reverse:  # instance would be Book
        if action == "post_add":
            book_authors = instance.authors.all()
            refresh_author_book_count(book_authors)

        if action == "pre_remove":
            global author_list
            author_list = set(instance.authors.all())

        if action == "post_remove":
            author_list.update(instance.authors.all())
            refresh_author_book_count(author_list)

    else:  # instance would be Author
        if action == "post_add" or action == "post_remove":
            instance.book_count = instance.books_authored.count()
            instance.save()


def refresh_author_book_count(authors):
    for author in authors:
        author.book_count = author.books_authored.count()
        author.save()
