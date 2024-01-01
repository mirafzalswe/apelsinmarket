from django.db import models
from django.contrib.auth.models import User
class Products(models.Model):
    product_image = models.FileField(upload_to='images/')
    price = models.IntegerField()
    title = models.CharField(max_length=255)
    product_info = models.TextField()
    date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"@{self.author}: {self.title}"
