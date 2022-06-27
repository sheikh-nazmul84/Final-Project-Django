from django import forms
from buying.models import Buying

class BuyingForm(forms.ModelForm):
    class Meta:
        model = Buying
        fields = "__all__"