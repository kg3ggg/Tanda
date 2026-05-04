from django.db import models

skills = [("skill1", "Креативность"),
             ("skill2", "Визуальное мышление"), 
             ("skill3", "Логика"), 
             ("skill4", "Аналитика"), 
             ("skill5", "Организация"), 
             ("skill6", "Структурирование")]


class Profession(models.Model):
    skill = models.CharField(choices=skills, verbose_name="Навык")  
    profession = models.CharField(max_length=255, verbose_name="Профессия") 
    image = models.ImageField(upload_to='tanda/photos/%Y/%m', verbose_name="Изображение")
    reason = models.TextField(verbose_name="Причина")
    description = models.TextField(verbose_name="Описание")
    
    
    class Meta:
        verbose_name = "Профессия"
        verbose_name_plural = "Профессии"
    
    def __str__(self):
        return self.skill + " - " + self.profession    