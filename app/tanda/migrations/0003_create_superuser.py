from django.db import migrations
import os

def create_superuser(apps, schema_editor):
    from django.contrib.auth.models import User
    
    # Читаем логин и пароль из переменных Railway (или используем admin/admin по умолчанию)
    username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
    password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'admin')
    email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
    
    # Создаем суперпользователя, если его еще нет
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username, email, password)

class Migration(migrations.Migration):

    dependencies = [
        ('tanda', '0002_profession'),
    ]

    operations = [
        migrations.RunPython(create_superuser),
    ]
