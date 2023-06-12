from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ContactUs, CateringBook, EventBook
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


class DateInput(forms.DateTimeInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class CateringForm(forms.ModelForm):
    class Meta:
        model = CateringBook
        fields = ('full_name', 'email', 'phone','event_date','event_time','event_address','time_of_arrival','food_served','estimated_no_of_guest','event_name','event_theme')

        labels= {
            'full_name':'Full Name:',
            'phone':'Phone:',
            'email':'Email:',
            'event_date':'Event Date:',
            'event_time':'Event Time:',
            'event_address': 'Event Address:',
            'time_of_arrival': 'Time of Arrival:',
            'food_served': 'Time the Food will be served:',
            'estimated_no_of_guest': 'Estimated No. of Guests:',
            'event_name': 'Event Name:',
            'event_theme': 'Event Theme:',
        }

        widgets = {
            'full_name': forms.TextInput(attrs={'class':'form-control','placeholder':'John Doe'}),
            'phone': forms.NumberInput(attrs={'class':'form-control','placeholder':'Phone'}),
            'email': forms.EmailInput(attrs={'class':'form-control','placeholder':'example@example.com'}),
            'event_date': DateInput(attrs={'class':'form-control'}),
            'event_time': TimeInput(attrs={'class':'form-control'}),
            'event_address': forms.TextInput(attrs={'class':'form-control','placeholder':'Address'}),
            'time_of_arrival': TimeInput(attrs={'class':'form-control'}),
            'food_served': TimeInput(attrs={'class':'form-control'}),
            'estimated_no_of_guest': forms.NumberInput(attrs={'class':'form-control','placeholder':'No.of Guests'}),
            'event_name': forms.TextInput(attrs={'class':'form-control'}),
            'event_theme': forms.TextInput(attrs={'class':'form-control'}),
        }
    # name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    # phone = forms.CharField(widget=forms.NumberInput(attrs={'placeholder': 'Phone'}))
    # email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.layout = Layout(
    #         Row(
    #             Column('name', css_class='col-md-6'),
    #             Column('phone', css_class='col-md-6'),
    #             Column('email', css_class='col-12'),
    #             css_class='row g-3'
    #         ),
    #         Submit('submit', 'Sign in')
    #     )


class EventManagementForm(forms.ModelForm):

    class Meta:
        model = EventBook
        fields = ('full_name', 'email', 'phone','event_date','event_time','event_address','time_of_arrival','food_served','estimated_no_of_guest','event_name','event_theme')


        labels= {
            'full_name':'Full Name:',
            'phone':'Phone:',
            'email':'Email:',
            'event_date':'Event Date:',
            'event_time':'Event Time:',
            'event_address': 'Event Address:',
            'time_of_arrival': 'Time of Arrival:',
            'food_served': 'Time the Food will be served:',
            'estimated_no_of_guest': 'Estimated No. of Guests:',
            'event_name': 'Event Name:',
            'event_theme': 'Event Theme:',
        }

        widgets = {
            'full_name': forms.TextInput(attrs={'class':'form-control','placeholder':'John Doe'}),
            'phone': forms.NumberInput(attrs={'class':'form-control','placeholder':'Phone'}),
            'email': forms.EmailInput(attrs={'class':'form-control','placeholder':'example@example.com'}),
            'event_date': DateInput(attrs={'class':'form-control'}),
            'event_time': TimeInput(attrs={'class':'form-control'}),
            'event_address': forms.TextInput(attrs={'class':'form-control','placeholder':'Address'}),
            'time_of_arrival': TimeInput(attrs={'class':'form-control'}),
            'food_served': TimeInput(attrs={'class':'form-control'}),
            'estimated_no_of_guest': forms.NumberInput(attrs={'class':'form-control','placeholder':'No.of Guests'}),
            'event_name': forms.TextInput(attrs={'class':'form-control'}),
            'event_theme': forms.TextInput(attrs={'class':'form-control'}),
        }

# class CheckoutForm(forms.ModelForm):

#     class Meta:
#         model = Checkout
#         fields = ('full_name', 'email', 'phone')

#         labels= {
#             'full_name':'Full Name:',
#             'phone':'Phone:',
#             'email':'Email:',
#         }

#         widgets = {
#             'full_name': forms.TextInput(attrs={'class':'form-control','placeholder':'John Doe'}),
#             'phone': forms.NumberInput(attrs={'class':'form-control','placeholder':'Phone'}),
#             'email': forms.EmailInput(attrs={'class':'form-control','placeholder':'example@example.com'}),
#         }