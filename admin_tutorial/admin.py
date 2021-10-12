from django.contrib import admin

from admin_tutorial.models import Book
from .models import Book

# Register your models here.
admin.site.register(Book)