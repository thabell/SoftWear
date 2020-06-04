from django import forms
from django.contrib.auth.models import User
from .models import Review, Refund


class UserForm(forms.ModelForm):
    password = forms.CharField(label="Пароль:", widget=forms.PasswordInput, required=True)
    password_double = forms.CharField(label="Повторно пароль:", widget=forms.PasswordInput, required=True)
    email = forms.CharField(label="E-mail", widget=forms.EmailInput, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password_double', 'email')

    def clean(self):
        cleaned_data = super().clean()
        passw = cleaned_data['password']
        passw_doub = cleaned_data['password_double']
        if passw != passw_doub:
            raise forms.ValidationError("Пароли не совпадают")
        return cleaned_data


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ("item", "comment")


class RefundForm(forms.ModelForm):
    class Meta:
        model = Refund
        fields = ("item", "comment")
