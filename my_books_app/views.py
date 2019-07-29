from django.shortcuts import render #Render means you don't need the HttpResponse, or HttpResponseRedirect.
from django.http import HttpResponseRedirect
from my_books_app.models import *

def index(request):
    return HttpResponseRedirect('/books')


def all(request):
    our_books = Book.objects.all()
    context = { 'our_books': our_books }
    return render(request, 'all.html', context)


def show(request, id): #Passing in the ID in the URL address.
    our_book = Book.objects.get(pk=id)
    context = {'our_book': our_book}
    return render(request, 'show.html', context)