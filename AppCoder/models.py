from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Profesion(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.nombre}'



class Avatar(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
   
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)

    def __str__(self):
        return f"Imagen de: {self.user}"


class Tag (models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = RichTextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="post", default="placeholder.png")
    state = models.BooleanField('Active',default=False)
    tags = models.ManyToManyField(Tag, null=True, blank=True)

    def __str__(self):
	    return self.title