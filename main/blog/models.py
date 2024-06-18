from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.title
