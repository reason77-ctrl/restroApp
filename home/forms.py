from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ContactUs
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name','last_name','email','password1','password2')


    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        # self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 100 characters or fewer. Letters, digits and @/./+/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        # self.fields['password1'].help_text = '<ul class="form-text text-muted"><small>Your password can\'t be too similar to your other things.</small></span>'
        
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''


class ContactForm(ModelForm):
    class Meta:
        model = ContactUs
        fields = ('name', 'email', 'phone', 'message')

        labels= {
            'name':'Full Name:',
            'email':'Email:',
            'phone':'Phone:',
            'message':'Message:',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'John Doe'}),
            'email': forms.EmailInput(attrs={'class':'form-control','placeholder':'example@example.com'}),
            'phone': forms.NumberInput(attrs={'class':'form-control','placeholder':'Phone'}),
            'message': forms.Textarea(attrs={'class':'form-control','placeholder':'Your Message'}),
        }


class CateringForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    phone = forms.CharField(widget=forms.NumberInput(attrs={'placeholder': 'Phone'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='col-md-6'),
                Column('phone', css_class='col-md-6'),
                Column('email', css_class='col-12'),
                css_class='row g-3'
            ),
            Submit('submit', 'Sign in')
        )


class EventManagementForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    phone = forms.CharField(widget=forms.NumberInput(attrs={'placeholder': 'Phone'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='col-md-6'),
                Column('phone', css_class='col-md-6'),
                Column('email', css_class='col-12'),
                css_class='row g-3'
            ),
            Submit('submit', 'Sign in')
        )