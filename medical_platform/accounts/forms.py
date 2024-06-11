from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Modality

class CustomUserCreationForm(UserCreationForm):
    work_rate = forms.ChoiceField(choices=[(1, '1'), (0.75, '0.75'), (0.5, '0.5')])
    primary_modality = forms.ModelChoiceField(queryset=Modality.objects.all())
    additional_modalities = forms.ModelMultipleChoiceField(queryset=Modality.objects.all(), required=False)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('work_rate', 'primary_modality', 'additional_modalities')

