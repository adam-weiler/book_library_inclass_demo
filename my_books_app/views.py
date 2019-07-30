from django.shortcuts import render #Render means you don't need the HttpResponse, or HttpResponseRedirect.
from django.http import HttpResponseRedirect
from my_books_app.models import Book, BookForm #This line changed. PM
# import pdb #This line is new. AM

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


def new(request): #This function is new. AM
    form = BookForm() #This function is new. PM
    # context = {"form": form} #Old Way
    context = {"form": form, "message":"Creating a new Book", "action":"/books/create"} #New Way
    # return render(request, 'new.html') #This line is new. AM
    # return render(request, 'new.html', context) #This line is new. PM
    return render(request, 'form.html', context) #This line is even newer. PM


def create(request): #This function is new. AM
    # breakpoint() #Then run request.POST

    #Old Way:
    # new_book = Book()
    # new_book.title = request.POST["title"]
    # new_book.author = request.POST["author"]
    # new_book.summary = request.POST["summary"]
    # new_book.save()

    #New Way:
    form = BookForm(request.POST) #This part is new. PM.

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/books')
        #The data has been submitted.
        #We could send them to thank you page.
        #Or send back to a list of books
    else:
        # breakpoint()
        context = {"form": form, "message":"Creating a new Book", "action":"/books/create"}

        return render(request, 'form.html', context)
        #There was an error. Returns to the form.html page with error.


def edit(request, id): #This function is new. AM
    our_book = Book.objects.get(pk=id) #Getting info from database, to prepopulate the form.

    #New Way:
    form = BookForm(instance=our_book) #This part is new. PM.

    # form.save() #Old Way - AM
    # context = {"book": our_book} #Old Way - AM
    
    # context = {"book": our_book, "form": form} #New Way - PM

    context = {"our_book": our_book, "form": form, "message":"Editing an existing Book", "action":f"/books/{our_book.pk}/update" } #Even Newer Way - PM

    return render(request, 'form.html', context)


def update(request, id): #This method is new. AM
    our_book = Book.objects.get(pk=id) #Getting info from database, to update it's data.

    #Old way
    # our_book.title = request.POST["title"]
    # our_book.author = request.POST["author"]
    # our_book.summary = request.POST["summary"]
    # our_book.save()

    #New way
    form = BookForm(request.POST, instance=our_book)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/books')
        #The data has been submitted.
        #We could send them to thank you page.
        #Or send back to a list of books
    else:
        # breakpoint()
        context = {"our_book": our_book, "form": form, "message":"Editing an existing Book", "action":f"/books/{our_book.pk}/update" }

        return render(request, 'form.html', context)
        #There was an error. Returns to the form.html page with error.


def delete(request, id): #This method is new. AM
    our_book = Book.objects.get(pk=id) #Getting info from database, to update it's data.
    our_book.delete()

    return HttpResponseRedirect('/books')
    #The data has been updated.
    #We could send them to thank you page.
    #Or send back to a list of books


#form.save() triggered
#typing:

#form   #Returns <BookForm bound=true, valid=Unknown, fields={title;author;summary;website)}

#form.is_valid()    #Returns False

#form.errors      #Returns {'website': ['Enter a valid URL.']}

