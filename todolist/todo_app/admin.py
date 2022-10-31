from django.contrib import admin
from .models import Task
# Register your models here.

@admin.register(Task)
class AddListModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'date','user', 'complete']
    