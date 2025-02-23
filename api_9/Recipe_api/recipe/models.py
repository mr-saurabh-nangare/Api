from django.db import models

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    ingredients = models.TextField(help_text="list ingredients saperated by commas ")
    instruction = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title