from django.db import models

# Create your models here.


class Author(models.Model):
    name=models.CharField(max_length=100)
    bio= models.TextField(max_length=500)

   




class post(models.Model):
    title = models.CharField(max_length=100)
    Publish_date=models.DateTimeField()
    content = models.TextField(max_length=15000)
    author= models.ForeignKey(Author,related_name='post_author',on_delete=models.CASCADE)

    def __str__(self):
        return self.title




