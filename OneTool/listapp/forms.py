from django import forms
from .models import Food, List

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ["foodname"]

class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ("item",)
        
