from django.contrib import admin
from unfold.admin import ModelAdmin
from tanda.models.professions import Profession


@admin.register(Profession)
class ProfessionAdmin(ModelAdmin):
    list_display = ("title", "skill", "image")
    search_fields = ("title", "skill", "reason", "description")
    list_filter = ("skill",)
    fields = ("title", "skill", "image", "reason", "description")
    ordering = ("title",)
