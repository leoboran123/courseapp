from django.contrib import admin
from .models import Course, Categorie, Slider

@admin.register(Course)

class CourseAdmin(admin.ModelAdmin):
    list_display = ("title","isActive","isHome","date","slug","category_list",)
    list_display_links = ("title","slug")
    prepopulated_fields = {"slug":("title",),}
    list_filter = ("isActive","isHome")
    list_editable = ("isActive","isHome")
    search_fields = ("title","description")

    def category_list(self, obj):
        html = ""
        
        for category in obj.categories.all():
            html += category.title + " "
        
        return html

@admin.register(Categorie)

class CategorieAdmin(admin.ModelAdmin):
    list_display = ("title","isActive","slug","courses")
    prepopulated_fields = {"slug":("title",),}
    list_editable = ("isActive",)

    def courses(self, obj):
        
        
        return obj.course_set.count()

admin.site.register(Slider)
