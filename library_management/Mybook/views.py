from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Book
from .forms import BookForm


def home(request):
    return render(request, 'home.html')


def display_books(request):
    books = Book.objects.all()
    return render(request, 'display_books.html', {'books': books})

@login_required(login_url='login')
def update_books(request):
    books = Book.objects.all()
    return render(request, 'update_books.html', {'books': books})

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return redirect('signup')

        User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, "Registration successful! Please login.")
        return redirect('login')

    return render(request, 'register.html')


def login_user(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not email or not password:
            messages.error(request, "Both fields are required!")
            return redirect('login')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, "Invalid email or password!")
            return redirect('login')

        user = authenticate(request, username=user.username, password=password)

        if user:
            login(request, user)
            return redirect('update_books')
        else:
            messages.error(request, "Invalid email or password!")

    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('update_books')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})


@login_required(login_url='login')
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    messages.success(request, "Book deleted successfully!")
    return redirect('update_books')
