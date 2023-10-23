from django import forms
from .models import *
class TalabaForm(forms.Form):
    i = forms.CharField(label="ism", max_length=30, min_length=3)
    k = forms.IntegerField(label="kursi", max_value=5)
    k_s = forms.IntegerField(label="kitoblar_soni")

class MuallifForm(forms.ModelForm):
    class Meta:
        model = Muallif
        fields = "__all__"  # ["ism", "kitoblar_soni", "tirik"]

class KitobForm(forms.ModelForm):
    class Meta:
        model = Kitob
        fields = "__all__"




