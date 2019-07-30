from django.db import models #Gives access to the ORM from Django
from django.forms import ModelForm #This line is new. PM

# from django.core.validators import URLValidator
# from django.core.exceptions import ValidationError

# class SlugField(CharField):
#     default_validators = [validators.validate_slug]


# from django.forms import URLField

from django.core.validators import MinValueValidator, URLValidator 
#TODO Min-Value-Validator

# class UrlField(DefaultUrlField):
#     default_validators = [URLValidator(regex=myregex)]


class Book(models.Model): #Gives us special functionality to talk to the ORM.
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    summary = models.TextField(null=True)
    # number_of_pages = models.IntegerField()
    # website = URLField()
    website = models.TextField(validators=[URLValidator()], null=True) #Our method
    pages = models.IntegerField(validators=[MinValueValidator(10)], null=True)
    website_alternative_way = models.URLField(max_length=250, null=True) #Eric's method
    

    def __str__(self):
        return f'{self.title} by {self.author}'

class BookForm(ModelForm): #This method is new. PM
    class Meta:
        model = Book #We want it tied to the model Book.
        fields = ['title', 'author', 'summary', 'website', 'pages', 'website_alternative_way']