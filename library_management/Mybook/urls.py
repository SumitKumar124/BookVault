from django.urls import path
from .views import home, display_books, update_books, add_book, delete_book, register, login_user, logout_user

urlpatterns = [
    path('', home, name='home'),
    path('books/', display_books, name='display_books'),
    path('update-books/', update_books, name='update_books'),
    path('add-book/', add_book, name='add_book'),
    path('delete-book/<int:book_id>/', delete_book, name='delete_book'),
    path('register/', register, name='signup'), 
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]
