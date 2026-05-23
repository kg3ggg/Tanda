#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
django.setup()

from tanda.models.tanda import Question

count = Question.objects.count()
print(f'Вопросов в БД: {count}')

# Запустим load_test_data еще раз
print('\n=== Запускаю load_test_data еще раз ===')
from django.core.management import call_command
call_command('load_test_data')

new_count = Question.objects.count()
print(f'\nВопросов после повторного запуска: {new_count}')

if new_count == count:
    print('✓ Дублирования нет - get_or_create работает правильно!')
else:
    print(f'✗ Данные дублировались! Было {count}, стало {new_count}')
