from django.db import models

# Create your models here.

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    about=models.TextField()
    type = models.CharField(max_length=100, choices=(('IT', 'IT'),
                                                     ('Non IT', 'Non IT'), 
                                                     ('Mobiles Phones', 'Mobile Phones')))
    added_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)


    def __str__(self) -> str:
        return self.name


class Employee(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=12)
    about=models.TextField()
    position=models.CharField(max_length=20, choices=(('designer', 'Designer'), 
                                                      ('developer', 'Developer'), 
                                                      ('data scientist', 'Data Scientist')))
    
    company=models.ForeignKey(Company, on_delete=models.CASCADE)