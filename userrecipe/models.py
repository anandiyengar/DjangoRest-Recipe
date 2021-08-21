from user.models import UserModel
from django.db import models

# Create your models here.


class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    diet = models.ManyToManyField('DietModel')
    calories = models.PositiveIntegerField()
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')


    def __str__(self):
        return self.title


class UpVote(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return self.recipe

class Comments(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return self.recipe


class DietModel(models.Model):
    diet = models.CharField(max_length=255)
    calories = models.CharField(max_length=255)

    def __str__(self):
        return self.diet