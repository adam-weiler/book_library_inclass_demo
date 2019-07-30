"""my_books_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from my_books_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('books/', views.all),
    # path('books/<str:something>', views.something), #This line is problematic. It would run before new, create. AM
    path('books/new', views.new), #This line is new. AM
    path('books/create', views.create),  #This line is new. AM
    path('books/<int:id>/update', views.update),  #This line is new. AM
    path('books/<int:id>', views.show),
    path('books/<int:id>/edit', views.edit),  #This line is new. AM
    path('books/<int:id>/delete', views.delete),  #This line is new. AM
]
