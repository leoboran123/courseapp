from django.contrib import admin
from .models import Course, Categorie

@admin.register(Course)

class CourseAdmin(admin.ModelAdmin):
    list_display = ("title","isActive","date","slug")
    list_display_links = ("title","slug")
    readonly_fields = ("slug",)
    list_filter = ("isActive",)
    list_editable = ("isActive",)
    search_fields = ("title","description")


@admin.register(Categorie)

class CategorieAdmin(admin.ModelAdmin):
    pass


