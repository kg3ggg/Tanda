#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
django.setup()

from tanda.models.professions import Profession

profs = Profession.objects.all()
print(f'Всего профессий: {profs.count()}')
print()

for prof in profs:
    image_status = 'есть' if prof.image else 'нет'
    print(f'✓ {prof.title}')
    print(f'  Скилл: {prof.get_skill_display()}')
    print(f'  Изображение: {image_status}')
    if prof.image:
        print(f'  URL: {prof.image.url if hasattr(prof.image, "url") else prof.image.name}')
    print()
