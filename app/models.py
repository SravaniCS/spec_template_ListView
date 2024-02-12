from django.db import models
from django.urls import reverse
# Create your models here.

class School(models.Model):
    sname=models.CharField(max_length=100)
    sprincipal=models.CharField(max_length=100)
    sloc=models.CharField(max_length=100)

    def __str__(self):
        return self.sname

    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})

class Student(models.Model):
    stname=models.CharField(max_length=100)
    rollno=models.IntegerField()
    sname=models.ForeignKey(School,on_delete=models.CASCADE,related_name='students')
    #related_name is used to fetch the data from child table without using child table name but by using the parent table object

    def __str__(self):
        return self.stname