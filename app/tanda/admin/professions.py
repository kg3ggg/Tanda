from django.contrib import admin
from unfold.admin import ModelAdmin
from ..models.professions import Profession


@admin.register(Profession)
class ProfessionAdmin(ModelAdmin):
    list_display = ("profession", "skill", "image", "reason", "description")
    search_fields = ("profession", "skill", "reason", "description")
    list_filter = ("skill",)
    fields = ("profession", "skill", "image", "reason", "description")
    ordering = ("profession",)
