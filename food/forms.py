from django import forms
from .models import item
# Ensure that the model name matches

class ItemForm(forms.ModelForm):
    class Meta:
        model = item
        fields = ['item_name', 'item_desc', 'item_price', 'item_image']
