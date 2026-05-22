from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from tanda.models.professions import Profession
import os
from pathlib import Path

# Сопоставление названий профессий с именами файлов изображений
IMAGE_MAPPING = {
    "Технологии и системы управления робототехникой": "robotics.jpg",
    "Правоведение": "law.jpg",
    "Преподавание в начальных классах и дошкольное образование": "teaching.jpg",
    "Финансы по отраслям": "finance.jpg",
    "Электроснабжение": "power.jpg",
    "Моделирование и конструирование швейных изделий": "fashion.jpg",
    "Налоги и налогообложение": "tax.jpg",
    "Техническое обслуживание и ремонт автомобильного транспорта": "auto.jpg",
    "Строительство и эксплуатация зданий и сооружений": "construction.jpg",
    "Менеджмент с китайским языком": "management.jpg",
}


class Command(BaseCommand):
    help = 'Связывает изображения с профессиями (файлы должны быть в tanda/static/professions/)'

    def handle(self, *args, **options):
        images_dir = Path(__file__).resolve().parent.parent.parent / 'static' / 'professions'
        
        self.stdout.write(f'📁 Проверяю папку: {images_dir}')
        
        if not images_dir.exists():
            self.stdout.write(self.style.ERROR(f'❌ Папка не найдена: {images_dir}'))
            self.stdout.write('Создай папку и добавь изображения с названиями:')
            for prof_title, img_name in IMAGE_MAPPING.items():
                self.stdout.write(f'  - {img_name}')
            return
        
        updated_count = 0
        
        for profession in Profession.objects.all():
            # Ищем соответствующее изображение
            image_filename = IMAGE_MAPPING.get(profession.title)
            
            if not image_filename:
                self.stdout.write(f'⚠️  Нет правила для: {profession.title}')
                continue
            
            image_path = images_dir / image_filename
            
            if not image_path.exists():
                self.stdout.write(self.style.WARNING(f'⚠️  Файл не найден: {image_filename}'))
                continue
            
            # Читаем файл и сохраняем в БД
            with open(image_path, 'rb') as f:
                image_content = f.read()
            
            image_relative_path = f'tanda/photos/{image_filename}'
            profession.image.save(image_filename, ContentFile(image_content), save=True)
            
            self.stdout.write(self.style.SUCCESS(f'✓ {profession.title} → {image_filename}'))
            updated_count += 1
        
        self.stdout.write(self.style.SUCCESS(f'\n✓ Обновлено профессий: {updated_count}'))
        
        self.stdout.write('\n📝 Как добавить изображения:')
        self.stdout.write(f'1. Скачай изображения')
        self.stdout.write(f'2. Переименуй их согласно списку выше')
        self.stdout.write(f'3. Помести в папку: {images_dir}/')
        self.stdout.write(f'4. Запусти эту команду: python manage.py link_profession_images')
