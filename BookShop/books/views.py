from django.shortcuts import render
from django.views.generic.base import View

from .models import Book


class BooksView(View):
    """List of book"""

    def get(self, request):
        allBooks = Book.objects.all()
        return render(request, "book_list.html",
                      {
                          "allBooks": allBooks,
                      })
