
from sileo.forms import ModelForm
from product.models import *
from dataclasses import fields

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
