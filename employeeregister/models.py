from django.db import models

# Create your models here.

class Position(models.Model):
    title=models.CharField(max_length=25)

    def __str__(self):
        return self.title

class Employee(models.Model):
    FullName=models.CharField(max_length=50)
    EmpCode=models.CharField(max_length=5)
    MobileNo=models.CharField(max_length=15)
    Designation=models.ForeignKey(Position,on_delete=models.CASCADE)
