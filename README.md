📚 Library Management System

Overview
The **Library Management System** is a web application built with **Django** and **MySQL** to help manage books efficiently. The system allows **admins** to perform CRUD operations on books, while **students** can view the list of available books without authentication.

Features
- Admin Features (Requires Login)
- Register & Login (with authentication)
- Add a Book 
- Update Book Details
- Delete a Book
- Logout

Student Features
- View Available Books

Technology Used
- **Backend:** Django (Python)
- **Frontend:** Bootstrap, HTML, CSS
- **Database:** MySQL



🛠️ Installation & Setup
1️⃣ Clone the Repository
```sh
git clone https://github.com/yourusername/Library-Management-System.git
cd Library-Management-System
```

2️⃣ Create a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

4️⃣ Configure Database
Edit `settings.py` to connect to MySQL:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'library_db',
        'USER': 'your_mysql_user',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

5️⃣ Apply Migrations
```sh
python manage.py makemigrations
python manage.py migrate
```

6️⃣ Create Superuser (Admin Login)
```sh
python manage.py createsuperuser
```

7️⃣ Run the Server
```sh
python manage.py runserver
```

📌 Usage
1. **Go to:** `http://127.0.0.1:8000/`
2. **View Books**
3. **Login as Admin**  (`http://127.0.0.1:8000/login/`)
4. **Manage Books**
5. **Logout when done** 

🤝 Contributing
Feel free to **fork** the repository, raise **issues**, or submit **pull requests**. Contributions are always welcome! 🚀



