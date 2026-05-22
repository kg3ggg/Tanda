#!/usr/bin/env python
import urllib.request
import urllib.error
import json
import sys

try:
    print("🔗 Проверяю API эндпоинт...")
    req = urllib.request.Request('http://localhost:8000/api/tanda/professions/')
    
    with urllib.request.urlopen(req, timeout=3) as response:
        if response.status == 200:
            print("✓ API доступен")
            data = json.loads(response.read().decode())
            print(f"✓ Получено профессий: {len(data)}")
            
            if data:
                first = data[0]
                print(f"\n📝 Первая профессия:")
                print(f"  Title: {first.get('title', '?')[:50]}")
                if first.get('image'):
                    print(f"  Image URL: {first.get('image')}")
                else:
                    print("  ✗ Image field пуст!")
                
                # Показываем все профессии с изображениями
                print(f"\n📊 Все профессии:")
                for i, prof in enumerate(data, 1):
                    img_status = "✓" if prof.get('image') else "✗"
                    print(f"  {i}. [{img_status}] {prof.get('title', '?')[:40]}")
        else:
            print(f"✗ Ошибка API: {response.status}")
        
except urllib.error.URLError as e:
    print("✗ API недоступен - запусти: python manage.py runserver")
    print(f"  Детали: {e}")
except Exception as e:
    print(f"✗ Ошибка: {e}")
    sys.exit(1)
