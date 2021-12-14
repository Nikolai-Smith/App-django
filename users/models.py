from django.db import models
from phone_field import PhoneField
# Create your models here.
class User(models.Model):
    first_name = models.CharField('Nome',max_length=50, null=False, blank=False)
    last_name = models.CharField('Sobrenome',max_length=50, null=False, blank=False)
    email = models.EmailField('E-mail', null=False, blank=False,unique=True)
    phone_number = PhoneField('Celular',blank=True)

    def  __str__(self):
        return self.first_name +" "+ self.last_name