from django.shortcuts import render #Render means you don't need the HttpResponse, or HttpResponseRedirect.
from django.http import HttpResponseRedirect
from my_books_app.models import *
# import pdb #This line is new

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


def new(request): #This function is new.
    return render(request, 'new.html')

def create(request): #This function is new.
    # breakpoint() #Then run request.POST
    new_book = Book()
    new_book.title = request.POST["title"]
    new_book.author = request.POST["author"]
    new_book.summary = request.POST["summary"]
    new_book.save()

    return HttpResponseRedirect('/books')
    #The data has been submitted.
    #We could send them to thank you page.
    #Or send back to a list of books

def edit(request, id): #This function is new.
    our_book = Book.objects.get(pk=id) #Getting info from database, to prepopulate the form.
    context = {"book": our_book}

    return render(request, 'edit.html', context)

def update(request, id):
    our_book = Book.objects.get(pk=id) #Getting info from database, to update it's data.
    our_book.title = request.POST["title"]
    our_book.author = request.POST["author"]
    our_book.summary = request.POST["summary"]
    our_book.save()

    return HttpResponseRedirect('/books')
    #The data has been updated.
    #We could send them to thank you page.
    #Or send back to a list of books

def delete(request, id):
    our_book = Book.objects.get(pk=id) #Getting info from database, to update it's data.
    our_book.delete()

    return HttpResponseRedirect('/books')
    #The data has been updated.
    #We could send them to thank you page.
    #Or send back to a list of books
