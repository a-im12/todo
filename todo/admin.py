from django.contrib import admin

from todo.models import TodoPost

class TodoPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    list_display_links = ('id', 'user')

admin.site.register(TodoPost, TodoPostAdmin)
