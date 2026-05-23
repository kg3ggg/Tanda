#!/usr/bin/env python
import os
import django
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
django.setup()

from tanda.models.professions import Profession

print('=== Проверка idempotency load_professions ===\n')

# Перед тестом
count_before = Profession.objects.count()
print(f'Профессий в БД до запуска: {count_before}')

# Первый запуск
print('\n--- Первый запуск load_professions ---')
call_command('load_professions', verbosity=0)
count_after_first = Profession.objects.count()
print(f'Профессий в БД после первого запуска: {count_after_first}')

# Второй запуск
print('\n--- Второй запуск load_professions ---')
call_command('load_professions', verbosity=0)
count_after_second = Profession.objects.count()
print(f'Профессий в БД после второго запуска: {count_after_second}')

# Проверка
print('\n=== РЕЗУЛЬТАТ ===')
if count_after_first == count_after_second:
    print(f'✓ УСПЕХ! Дублирования нет. Количество: {count_after_first}')
else:
    print(f'✗ ОШИБКА! Данные дублировались: {count_after_first} → {count_after_second}')
