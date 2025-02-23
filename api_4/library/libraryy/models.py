from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    pages=models.IntegerField(default=0)
    available = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    
class Member(models.Model):
    name = models.CharField(max_length=100)
    email =models.EmailField(unique=True)
    join_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Borrow(models.Model):
    member = models.ForeignKey(Member,on_delete=models.CASCADE)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    borrow_date =models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True,blank=True)
    
    def __str__(self):
        return f"{self.member.name} borrowed {self.book.title}"