from django import forms

from . import models


class CircleForm(forms.ModelForm):
    class Meta:
        model = models.Circle
        fields = "__all__"
        exclude = ['user']
