from django.db import models

# Create your models here.


class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)

class UserToken(models.Model):
    token = models.CharField(max_length=128)
    userinfo = models.OneToOneField(to="UserInfo")


class Publisher(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title=models.CharField(max_length=64)
    price = models.IntegerField()
    pub_date = models.DateField()
    publisher=models.ForeignKey(to='Publisher')
    authors = models.ManyToManyField(to="Author")
    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=48)
    age = models.IntegerField(default=2)
    def __str__(self):
        return self.name