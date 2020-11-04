from django import forms
from .models import Task
from django.forms.models import modelformset_factory

class UpdateStatusForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['done']

StatusFormSet = modelformset_factory(Task,form=UpdateStatusForm)