from django.contrib import admin

from .models import Board


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'content',
        'created_at',
        'updated_at',
        'weather',
    )
