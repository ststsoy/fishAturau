from django import forms 
from newsself.models import*
class AddphotoForm(forms.ModelForm):
    
    class Meta():
        model = Newsself
        fields ='__all__'