from django.db import models

from datetime import datetime

from django.urls import reverse

# Create your models here.


class Transfer(models.Model):

    cat = (
        ('MI', 'MI'),
        ('sport', 'sport'),
        ('eco', 'eco'),

    )
    CATEGORY = (
        ('L1', 'L1'),
        ('L2', 'L2'),
        ('L3', 'L3'),
        )


    spe_choice = models.CharField(max_length=200 , null=True , choices=cat)


    first_name = models.CharField(max_length=200,null=True)
    last_name = models.CharField(max_length=200,null=True)
    orginal_uni = models.CharField(max_length=400, null=True)
    level = models.CharField(max_length=10, null=True, choices=CATEGORY)
    email = models.EmailField(max_length = 254,null=True)
    phone_number = models.IntegerField(null=True)
    wilaya = models.CharField(max_length=200,null=True)
    birth_date = models.DateField(default=datetime.now)
    bac_mean = models.DecimalField(max_digits = 5,decimal_places = 2, default=10.00)
    bac_date = models.DateField(default=datetime.now)
    bac_number = models.IntegerField(default=1111111)
    files = models.FileField(null=True)
    approved = models.BooleanField(default = False)

    def __str__(self):
        return self.first_name + ' ' + self.last_name  + ' ' + self.level + ' ' + self.orginal_uni + ' ' + self.wilaya 

    



class Approval(models.Model):
    student = models.ForeignKey(Transfer, default=None , on_delete=models.CASCADE , null=True)
    approved = models.BooleanField(default = False)
    first_name = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.student.first_name + ' ' +  self.student.last_name 

    


    




