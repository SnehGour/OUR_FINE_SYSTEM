from django import forms
from FineSystemapp.models import Apply_Fine

class NewFineApply(forms.ModelForm):
    class Meta():
        model = Apply_Fine
        fields = '__all__'
