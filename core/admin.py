from django.contrib import admin

from core.models import author
from .models import author, Book

# Register your models here.

admin.site.register(author)
admin.site.register(Book)