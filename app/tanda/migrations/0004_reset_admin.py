from django.db import migrations

def force_reset_admin(apps, schema_editor):
    from django.contrib.auth.models import User
    
    # Ищем пользователя admin, если нет - создаем
    user, created = User.objects.get_or_create(username='admin')
    user.email = 'admin@example.com'
    # ЖЕСТКО ставим пароль admin
    user.set_password('admin')
    user.is_staff = True
    user.is_superuser = True
    user.save()

class Migration(migrations.Migration):

    dependencies = [
        ('tanda', '0003_create_superuser'),
    ]

    operations = [
        migrations.RunPython(force_reset_admin),
    ]
