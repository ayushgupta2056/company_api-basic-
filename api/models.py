from django.db import models

# Create your models here.
class company(models.Model):
    company_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    about=models.TextField()
    add_date=models.DateTimeField(auto_now=True)
    type=models.CharField(max_length=100,choices=(('IT','IT'),
                          ('finance','ca')))
    

class employee(models.Model):
    age=models.CharField(max_length=50)
    about=models.TextField()
    add_date=models.DateTimeField()
    type=models.CharField(max_length=100,choices=(('IT','IT'),
                          ('finance','ca')))
    
    company=models.ForeignKey(company,on_delete=models.CASCADE)