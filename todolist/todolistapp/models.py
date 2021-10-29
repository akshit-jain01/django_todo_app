from django.db import models
from rest_framework import serializers


# Create your models here.


class Task(models.Model):
    taskTitle = models.CharField(max_length = 50)
    picture = models.ImageField()
    taskDescription = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    bookmark = models.BooleanField(default=False)

    def __str__(self):
        return self.taskTitle


class Collections(models.Model):
    collection = models.CharField(max_length=30)
    task = models.ManyToManyField(Task, through='Enrollment')

    def __str__(self):
        return self.collection


class Enrollment(models.Model):
    title = models.ForeignKey(Task, on_delete=models.CASCADE)
    collection = models.ForeignKey(Collections, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['title','collection']]


