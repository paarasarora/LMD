from django.urls import path
from .views import *
app_name = 'books'

# from books.views import BooksViewSet

# router = DefaultRouter()
# router.register('books',BooksViewSet,basename='books')
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('books',include('accounts.'))
    # path('api/',include(router.urls))
# ]