from .models import Products
from django.forms import ModelForm

class ProductAddForm(ModelForm):
    class Meta:
        model = Products
        fields = ['product_image', 'title','price', 'product_info']

