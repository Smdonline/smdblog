from django import forms
from .models import Work
from captcha.fields import ReCaptchaField
class BootsrapFormMixin(object):

    input_class = None

    def __init__(self,*args,**kwargs):
        super(BootsrapFormMixin,self).__init__(*args,**kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = self.input_class
class MessageForm(BootsrapFormMixin,forms.ModelForm):
    captcha = ReCaptchaField()
    input_class = 'form-control'
    class Meta:
        model = Work
        fields = ('name','email','phone','message')
    def clean_name(self):
        name=self.cleaned_data.get('name')
        if len(name)<6:
            raise  forms.ValidationError(_('name too short at least 6 characters'))
        return name
    def clean_message(self):
        message=self.cleaned_data.get('message')
        if len(message)<100:
            raise forms.ValidationError(_('message must be larger then 100 characters you insert only {}').format(len(message)))
        return message