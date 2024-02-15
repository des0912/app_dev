from django.contrib import admin
from .models import post

@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slus', 'author', 'publish', 'status'] #para makita sa lalabas sa list
    list_filter = ['status', 'create', 'publish', 'author']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title')}
    row_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    
# Register your models here.
