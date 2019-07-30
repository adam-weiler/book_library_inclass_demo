from django.db import models #Gives access to the ORM from Django
from django.forms import ModelForm #This line is new. PM

class Book(models.Model): #Gives us special functionality to talk to the ORM.
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    summary = models.TextField(null=True)

    def __str__(self):
        return f'{self.title} by {self.author}'

class BookForm(ModelForm): #This method is new. PM
    class Meta:
        model = Book #We want it tied to the model Book.
        fields = ['title', 'author', 'summary']