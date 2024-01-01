from PIL.Image import Image
from django.db import models
from django.contrib.auth.models import User
from django import  forms
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField()
    avatar = models.ImageField(upload_to='customers/', default='default/default.jpg')

    def __str__(self):
        return f"@{self.user.username}"



class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['about', 'avatar']
