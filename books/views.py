from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class BooksViewSet(ModelViewSet):
    serializer_class = BooksSerializer
    queryset = Books.objects.all()
    permission_classes = [IsAuthenticated]
    
    def create(self,request,*args,**kwargs):
        user = request.user
        if user.user_type == "FACULTY":
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)   
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        raise ValidationError({'message':['librarian can only add']})
    def destroy(self, request,*args, **kwargs):
        obj = self.get_object()
        user = request.user
        if user.user_type == "FACULTY":
            book_fk = Members.objects.filter(book = obj.id).last()
            if not book_fk:  
                obj.delete()
            else:
                book_fk.book = None
                book_fk.save()
                obj.delete()
            return Response({'message':'Book deleted'},status = status.HTTP_204_NO_CONTENT)
        raise ValidationError({'message':'only librarian can delete a book'})
    def update(self,request,*args, **kwargs):
        user = request.user
        obj = self.get_object()
        if user.user_type == "FACULTY":
            serializer = self.get_serializer(obj,data = request.data,partial = True)
            serializer.is_valid(raise_exception = True)
            serializer.save()
            return Response(serializer.data)
        raise ValidationError({'message':'only librarian can update the book'})

class MembersViewSet(ModelViewSet):
    serializer_class = MembersSerializers
    queryset = Members.objects.all()
    permission_classes = [IsAuthenticated]

    def create(self,request,*args,**kwargs):
            user = request.user
            if user.user_type == "FACULTY":
                user_obj = self.queryset.filter(user = request.data.get('user')).last()
                if not user_obj:
                    obj = self.queryset.filter(book =request.data.get('book')).last()
                    if not obj:
                        serializer = self.get_serializer(data=request.data)
                        serializer.is_valid(raise_exception=True)
                        self.perform_create(serializer)   
                        book_obj = Books.objects.filter(id = request.data.get('book')).last()
                        book_obj.status = 'BORROWED'
                        book_obj.save()
                        return Response(serializer.data,status = status.HTTP_201_CREATED)
                    raise ValidationError({'message':'book already borrowed'})
                raise ValidationError({'message':'user already exists'})
            raise ValidationError({'message':'Students cannot add other members'})

    def destroy(self, request,*args, **kwargs):
        obj = self.get_object()
        user = request.user
        if user.user_type == "FACULTY":
            obj.delete()  
            return Response({'message':'Member deleted'},status = status.HTTP_204_NO_CONTENT)
        raise ValidationError({'message':'only librarian can delete a member'})

    def update(self,request,*args, **kwargs):
        user = request.user
        obj = self.get_object()
        if user.user_type == "FACULTY":
            serializer = self.get_serializer(obj,data = request.data,partial = True)
            serializer.is_valid(raise_exception = True)
            serializer.save()
            return Response(serializer.data)
        if user.user_type == 'STUDENT':
            obj_book = Books.objects.filter(id = request.data.get('book')).last()
            if obj_book:
                print(obj_book.status)
                if obj_book.status == 'AVAILABLE':
                    if request.data.get('book') and obj_book.status == 'AVAILABLE':
                        obj_book.status = 'BORROWED'
                        obj_book.save()
                        if obj.book:
                            obj.book.status = 'AVAILABLE'
                            obj.book.save()
                else:
                    raise ValidationError({'message':'borrowed book cannot be reissued'})
            else:
                if obj.book:
                    obj.book.status = 'AVAILABLE'
                    obj.book.save()
                    obj.book = None
            
            serializer = self.get_serializer(obj,data = request.data,partial = True)
            serializer.is_valid(raise_exception = True)
            serializer.save()
            return Response(serializer.data)
    

    

