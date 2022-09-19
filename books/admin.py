from django.contrib import admin

from books.models import Books, Members

# Register your models here.

admin.site.register(Books)
admin.site.register(Members)
