from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Modality

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    primary_modality = forms.ModelChoiceField(queryset=Modality.objects.all(), required=True)
    additional_modalities = forms.ModelMultipleChoiceField(queryset=Modality.objects.all(), required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'work_rate', 'primary_modality', 'additional_modalities']

