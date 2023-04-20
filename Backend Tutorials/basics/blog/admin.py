from django.contrib import admin
from blog.models import Post

# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug','author')
admin.site.register(Post, AuthorAdmin)
