from django import forms
from .models import CadastroLanding

class CadastroLandingForm(forms.ModelForm):
    class Meta:
        model = CadastroLanding
        fields = ['nome','email']