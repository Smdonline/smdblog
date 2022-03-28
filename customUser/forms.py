from django.contrib.auth.forms import (
    ReadOnlyPasswordHashField,AuthenticationForm, PasswordResetForm,
    SetPasswordForm, PasswordChangeForm
)
from captcha.fields import ReCaptchaField
from django import forms
from.models import MyUser,Profil
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from .tokens import account_activation_token
from django.core.mail import EmailMessage
class BootsrapFormMixin(object):

    input_class = None

    def __init__(self,*args,**kwargs):
        super(BootsrapFormMixin,self).__init__(*args,**kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = self.input_class
class UserCreationForm(BootsrapFormMixin,forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    captcha = ReCaptchaField()
    input_class = 'form-control'
    class Meta:
        model = MyUser
        fields = ('email',)


    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        if len(password2) < 8:
            raise forms.ValidationError('Password too short ')
        return password2

    def save(self,commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = ('email', 'password','first_name','last_name','is_active', 'is_admin')

    def clean_password(self):
        return self.initial["password"]


class MyPasswordChangeForm(BootsrapFormMixin, PasswordChangeForm):
    input_class = 'form-control'


class MyLoginForm(BootsrapFormMixin, AuthenticationForm):
    input_class = 'form-control'

class MyPasswordResetForm(BootsrapFormMixin,PasswordResetForm):
    input_class = 'form-control'

    # def send_mail(self, subject_template_name, email_template_name, context,
    #               from_email, to_email, html_email_template_name=None):
    #     context['user'] = context['user'].id
    #     send_mail.delay(subject_template_name=subject_template_name,
    #                     email_template_name=email_template_name,
    #                     context=context, from_email=from_email, to_email=to_email,
    #                     html_email_template_name=html_email_template_name)
class MyPasswordSetForm(BootsrapFormMixin,SetPasswordForm):
    input_class = 'form-control'

class ChangeUserProfile(BootsrapFormMixin,forms.ModelForm):
    input_class = 'form-control'
    class Meta:
        model=Profil
        exclude = ('user',)




