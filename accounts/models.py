from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
# Create your models here.
class User(AbstractUser):
    SUBTYPE_FACULTY = "FACULTY"
    SUBTYPE_STUDENT = "STUDENT"

    TYPE_CHOICES = (
        (SUBTYPE_FACULTY, 'FACULTY'),
        (SUBTYPE_STUDENT, 'STUDENT'),
    )
    name = models.CharField(max_length=200)
    user_type = models.CharField(choices=TYPE_CHOICES, max_length=20,default = 'STUDENT')
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []