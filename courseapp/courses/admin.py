from django.contrib import admin
from .models import Course, Categorie

@admin.register(Course)

class CourseAdmin(admin.ModelAdmin):
    list_display = ("title","isActive","date","slug","categorie")
    list_display_links = ("title","slug")
    prepopulated_fields = {"slug":("title",),}
    list_filter = ("isActive","categorie")
    list_editable = ("isActive",)
    search_fields = ("title","description")


@admin.register(Categorie)

class CategorieAdmin(admin.ModelAdmin):
    list_display = ("title","isActive","slug")
    prepopulated_fields = {"slug":("title",),}




