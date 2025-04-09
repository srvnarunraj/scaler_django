# Django Basics
Django Project by Scaler Tutor

# Setup
```bash
python3 -m django startproject ecommerce
django-admin startapp products
```

# Migrate Models
```bash
python3 manage.py makemigrations 
python3 manage.py migrate
python3 manage.py makemigrations products 
python3 manage.py migrate
```

# Admin Portal
```bash
python3 manage.py createsuperuser
```