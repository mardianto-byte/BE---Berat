# import form class from django
from django import forms
from .models import Berat
 
# create a ModelForm
class BeratForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Berat
        fields = "__all__"