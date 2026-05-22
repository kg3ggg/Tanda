#!/usr/bin/env python
"""
Создаёт плейсхолдер-изображения для каждой профессии
"""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

# Соответствие имён файлов и профессий
PROFESSIONS = {
    "robotics.jpg": "Робототехника",
    "law.jpg": "Право",
    "teaching.jpg": "Преподавание",
    "finance.jpg": "Финансы",
    "power.jpg": "Энергетика",
    "fashion.jpg": "Мода",
    "tax.jpg": "Налоги",
    "auto.jpg": "Авто",
    "construction.jpg": "Строительство",
    "management.jpg": "Менеджмент",
}

# Цвета для каждой профессии
COLORS = [
    "#FF6B6B", "#4ECDC4", "#45B7D1", "#FFA07A", "#98D8C8",
    "#F7DC6F", "#BB8FCE", "#85C1E2", "#F8B88B", "#82E0AA"
]

OUTPUT_DIR = Path(__file__).parent / "tanda" / "static" / "professions"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

print(f"📁 Создаю изображения в: {OUTPUT_DIR}")

for idx, (filename, profession_name) in enumerate(PROFESSIONS.items()):
    # Создаём изображение (600x400)
    img = Image.new('RGB', (600, 400), color=COLORS[idx])
    draw = ImageDraw.Draw(img)
    
    # Пытаемся использовать системный шрифт, если нет - используем дефолтный
    try:
        font = ImageFont.truetype("arial.ttf", 48)
        font_small = ImageFont.truetype("arial.ttf", 24)
    except:
        font = ImageFont.load_default()
        font_small = ImageFont.load_default()
    
    # Рисуем текст
    text = f"🎯\n{profession_name}\n(Placeholder)"
    # Простой способ - найти текст в центре
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (600 - text_width) // 2
    y = (400 - text_height) // 2
    
    # Белый текст с чёрной тенью
    draw.multiline_text((x+2, y+2), text, fill="black", font=font, align="center")
    draw.multiline_text((x, y), text, fill="white", font=font, align="center")
    
    # Сохраняем файл
    filepath = OUTPUT_DIR / filename
    img.save(filepath, quality=95)
    print(f"✓ {filename} → {profession_name}")

print(f"\n✓ Все {len(PROFESSIONS)} плейсхолдеров созданы!")
