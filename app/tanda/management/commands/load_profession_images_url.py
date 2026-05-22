from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from tanda.models.professions import Profession
import requests
from urllib.parse import urlparse
import os

# Сопоставление названий профессий с URL изображений
IMAGES_URLS = {
    "Технологии и системы управления робототехникой": "",  # Добавь URL сюда
    "Правоведение": "",
    "Преподавание в начальных классах и дошкольное образование": "",
    "Финансы по отраслям": "",
    "Электроснабжение": "",
    "Моделирование и конструирование швейных изделий": "",
    "Налоги и налогообложение": "",
    "Техническое обслуживание и ремонт автомобильного транспорта": "",
    "Строительство и эксплуатация зданий и сооружений": "",
    "Менеджмент с китайским языком": "",
}


class Command(BaseCommand):
    help = 'Загружает изображения для профессий по URL'

    def add_arguments(self, parser):
        parser.add_argument(
            '--url',
            type=str,
            help='URL для загрузки одного изображения'
        )
        parser.add_argument(
            '--title',
            type=str,
            help='Название профессии для привязки'
        )

    def handle(self, *args, **options):
        if options['url'] and options['title']:
            self.download_single_image(options['title'], options['url'])
        else:
            self.stdout.write('Используй флаги:')
            self.stdout.write('  python manage.py load_profession_images_url --title="<название>" --url="<ссылка>"')

    def download_single_image(self, title, url):
        try:
            profession = Profession.objects.get(title=title)
        except Profession.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'❌ Профессия не найдена: {title}'))
            return

        try:
            self.stdout.write(f'⬇️  Загружаю изображение для: {title}')
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            # Получаем имя файла из URL
            parsed_url = urlparse(url)
            filename = os.path.basename(parsed_url.path)
            if not filename or '.' not in filename:
                filename = f"{title.lower().replace(' ', '_')}.jpg"

            # Сохраняем в БД
            profession.image.save(filename, ContentFile(response.content), save=True)
            self.stdout.write(self.style.SUCCESS(f'✓ {title} ← {filename}'))

        except requests.exceptions.RequestException as e:
            self.stdout.write(self.style.ERROR(f'❌ Ошибка загрузки: {str(e)}'))
