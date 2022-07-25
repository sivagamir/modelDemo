from django.db import models

# Create your models here.
class Employee(models.Model):
    empNo=models.IntegerField()
    empName=models.CharField(max_length=25)
    empSalary=models.IntegerField()
    empAddress=models.CharField(max_length=50)
def __str__(self):
    return 'employee details are shared' + empName
