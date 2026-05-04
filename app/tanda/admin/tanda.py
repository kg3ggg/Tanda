from django.contrib import admin
from unfold.admin import ModelAdmin, StackedInline, TabularInline
from tanda.models.tanda import Question, Option

class OptionInline(StackedInline):
    model = Option
    extra = 1
    show_change_link = True 
    fields = ("value", "text",
              "skill1", "skill2", "skill3", "skill4", "skill5", "skill6")      
    verbose_name = "Ответ"
    verbose_name_plural = "Ответы"


@admin.register(Question)
class QuestionAdmin(ModelAdmin):
    list_display = ("text",)
    inlines = [OptionInline]
    