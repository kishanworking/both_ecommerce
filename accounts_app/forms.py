from django import forms 
from .models import Account



class RegistrationForm(forms.ModelForm):
    # for storing password                                css attributes
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password',
        'class': 'form-control',
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'confirm Password'
    }))


    class Meta:
        model = Account
        fields = ['first_name','last_name','phone_number','email','password']

     
    # adding placeholder and css class='form-control' to all the fields
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        
        # adding placeholder for each fields 
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter last Name'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter phone Number'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Email Address'
        
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            

    # checking if password and conform password 
    def clean(self):
        cleande_data = super(RegistrationForm, self).clean()
        password = cleande_data.get('password')
        confirm_password = cleande_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError( 
                "Password does not match!"
            )
        
    