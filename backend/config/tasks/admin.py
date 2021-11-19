from django.contrib import admin

from . import models

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ['user', 'name']
    list_filter = ['user']
    search_fields = ['name']


admin.site.register(models.Task, TaskAdmin)