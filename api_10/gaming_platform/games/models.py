from django.db import models

# Create your models here.
class Developer(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField(null=True, blank=True)
    
    def __str__(self):
        return self.name
class Game(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    release_date = models.DateField()
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE,related_name="games")
    
    def __str__(self):
        return self.title
class Review(models.Model):
    game =models.ForeignKey(Game, on_delete=models.CASCADE,related_name='reviews')
    reviewer_name = models.CharField(max_length=100)
    rating = models.PositiveIntegerField(choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')))
    comment = models.TextField()
    
    def __str__(self):
        return f"{self.reviewer_name} - {self.game.title}"