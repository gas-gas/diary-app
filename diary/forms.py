from django import forms
from .models import Day

class DayCreateFrom(forms.ModelForm):

    class Meta:
        model = Day
        fields = '__all__'
