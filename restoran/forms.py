from django import forms

from .models import MenuModel


class MenuForm(forms.ModelForm):
    class Meta:
        model = MenuModel
        fields = '__all__'
