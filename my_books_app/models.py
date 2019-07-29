from django.db import models #Gives access to the ORM from Django

class Book(models.Model): #Gives us special functionality to talk to the ORM.
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    summary = models.TextField(null=True)

    def __str__(self):
        return f'{self.title} by {self.author}'