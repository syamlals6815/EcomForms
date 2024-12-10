from django import forms
from .models import Category, Product

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Category'})
        }
        

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['category']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Name of Product'}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'Description'}),
            'product_image':forms.ClearableFileInput(attrs={'class':'form-control'}),
            'price':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Price'}),
            'stock':forms.NumberInput(attrs={'class':'form-control','placeholder':'Available Stock'}),
            
        }
        

