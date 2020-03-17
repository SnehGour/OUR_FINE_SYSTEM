from django import forms
from FineSystemapp.models import Fine_apply

class NewFineApply(forms.ModelForm):
    class Meta():
        model = Fine_apply
        fields = '__all__'
