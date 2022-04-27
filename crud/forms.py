from django import forms
from crud.models import Details

class CrudCreateForm(forms.ModelForm):
    class Meta:
        model = Details
        fields = '__all__'

        

class CrudUpdateForm(forms.ModelForm):
    class Meta:
        model = Details
        fields = '__all__'
   