from django.contrib.auth import get_user_model

User = get_user_model()
username = 'admin'
password = 'admin'
email = 'admin@example.com'

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print("Superuser created")
else:
    print("Superuser already exists")
