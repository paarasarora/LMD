from django.db import models

from accounts.models import User

# Create your models here.


class Books(models.Model):
    SUBTYPE_AVAILABLE = "AVAILABLE"
    SUBTYPE_BORROWED = "BORROWED"

    TYPE_CHOICES = (
        (SUBTYPE_AVAILABLE, 'AVAILABLE'),
        (SUBTYPE_BORROWED, 'BORROWED'),
    )
    name = models.CharField(max_length=200)
    status = models.CharField(choices=TYPE_CHOICES, max_length=20,default = 'AVAILABLE')
    def __str__ (self):
        return str(self.name)

class Members(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
    book = models.ForeignKey(Books,on_delete=models.DO_NOTHING,related_name='book', null=True,blank = True)
    name = models.CharField(max_length=200)
    def __str__ (self):
        return str(self.name)