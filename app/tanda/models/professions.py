from django.db import models

skills = [("skill1", "Креативность"),
             ("skill2", "Визуальное мышление"), 
             ("skill3", "Логика"), 
             ("skill4", "Аналитика"), 
             ("skill5", "Организация"), 
             ("skill6", "Структурирование")]


class Profession(models.Model):
    skill = models.CharField(choices=skills, verbose_name="Навык", max_length=10)  
    title = models.CharField(max_length=255, verbose_name="Профессия") 
    image = models.ImageField(upload_to='tanda/photos/%Y/%m', verbose_name="Изображение", blank=True, null=True)
    reason = models.TextField(verbose_name="Причина")
    description = models.TextField(verbose_name="Описание")
    
    
    class Meta:
        verbose_name = "Профессия"
        verbose_name_plural = "Профессии"
    
    def __str__(self):
        return f"{self.get_skill_display()} - {self.title}"    