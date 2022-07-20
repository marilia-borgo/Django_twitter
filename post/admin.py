from django.contrib import admin

from .models import Comentario, Post, Profile

# Register your models here.


class ComentarioInline(admin.TabularInline):  # new
    model = Comentario


class PostAdmin(admin.ModelAdmin):  # new
    inlines = [
        ComentarioInline,
    ]


admin.site.register(Post, PostAdmin)
admin.site.register(Comentario)
admin.site.register(Profile)
