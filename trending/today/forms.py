from django import forms
from .models import manunews,counter


class Test(forms.ModelForm):
    class Meta:
        model = manunews
        fields = '__all__'
class count(forms.ModelForm):
    class Meta:
        model = counter
        fields = '__all__'