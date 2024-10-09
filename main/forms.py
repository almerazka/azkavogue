from django import forms
from .models import Product
from django.core.exceptions import ValidationError
from django.utils.html import strip_tags

class ProductEntryForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'quantity', 'image']

    def clean_name(self):
        name = self.cleaned_data['name']
        cleaned_name = strip_tags(name).strip()
        if not cleaned_name:
            raise forms.ValidationError("This field cannot be blank")
        return cleaned_name

    def clean_description(self):
        description = self.cleaned_data['description']
        cleaned_description = strip_tags(description).strip()
        if not cleaned_description:
            raise forms.ValidationError("This field cannot be blank")
        return cleaned_description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price < 0:
            raise ValidationError('Price must be a positive number.')
        return price

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity is not None and quantity < 0:
            raise ValidationError('Quantity must be a positive integer.')
        return quantity
