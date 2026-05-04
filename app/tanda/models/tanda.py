from django.db import models

class Question(models.Model):
    text = models.TextField(verbose_name="Вопрос")

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

    def __str__(self):
        return self.text[:20]


class Option(models.Model):
    
    abc = [("A", "A"), ("B", "B"), ("C", "C"), ("D", "D")]
    
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="options",
        verbose_name="Вопрос"
    )
    value = models.CharField(
        max_length=1,
        choices=abc,
        verbose_name="Буква",
        default="A"
    )
    text = models.CharField(max_length=255, verbose_name="Ответ")

    skill1 = models.IntegerField(verbose_name="Креативность", default=0)
    skill2 = models.IntegerField(verbose_name="Визуальное мышление", default=0)
    skill3 = models.IntegerField(verbose_name="Логика", default=0)
    skill4 = models.IntegerField(verbose_name="Аналитика", default=0)
    skill5 = models.IntegerField(verbose_name="Организация", default=0)
    skill6 = models.IntegerField(verbose_name="Структурирование", default=0)
    
        
    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"

