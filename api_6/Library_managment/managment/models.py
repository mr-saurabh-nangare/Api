from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=False, unique=True)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=100,unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    publish_date = models.DateField()
    copies = models.IntegerField(default=1)
    
    def __str__(self):
        return self.name

class Borrower(models.Model):
    name= models.CharField(max_length=100)
    email = models.EmailField(null=False, unique=True)
    borrowed_book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True ,blank=True)
    
    def __str__(self):
        return self.name