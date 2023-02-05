from django.db import models
from django.utils.text import slugify

# Create your models here.



class Categorie(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    slug = models.SlugField(default="",blank=True,editable=True, null=False, unique=True, db_index=True)
    isActive = models.BooleanField()
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(args,kwargs)
    
    def __str__(self):
        return f"{self.title}"


class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    imageUrl = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)
    isActive = models.BooleanField()
    slug = models.SlugField(default="",blank=True, null=False, unique=True, db_index=True)
    categorie = models.ForeignKey(Categorie,null=True, default="", on_delete=models.CASCADE, related_name="kurslar")

    def __str__(self):
        return f"{self.title}"   