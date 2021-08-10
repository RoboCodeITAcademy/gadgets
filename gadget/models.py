from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,unique=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,unique=True)

    def __str__(self):
        return self.name

class Gadget(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name='categories')
    tag = models.ManyToManyField(Tag,related_name='tags')
    image = models.ImageField(upload_to='gadgets/')
    created = models.DateTimeField(auto_now_add=True)
    file_format = models.CharField(max_length=20)
    description = models.TextField(verbose_name='Description')

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created']
        verbose_name_plural = 'Gadgets'

    
