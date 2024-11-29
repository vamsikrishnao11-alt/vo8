from django.db import models

# Create your models here.
class Department(models.Model):
    sub=models.CharField(max_length=100,primary_key=True)
    fee=models.IntegerField()
    def __str__(self):
        return self.sub
class Student(models.Model):
    sub=models.ForeignKey(Department,on_delete=models.CASCADE)
    sname=models.CharField(max_length=100)
    num=models.IntegerField()
    paid=models.IntegerField()
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    def __str__(self):
        return self.sname
class Declaration(models.Model):
    sname=models.ForeignKey(Student,on_delete=models.CASCADE)
    code=models.CharField(max_length=100)
    verify=models.CharField(max_length=100)

