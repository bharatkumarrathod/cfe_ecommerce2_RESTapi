from django import forms
from .models import SignUp


class SignUpForm(forms.ModelForm):

    """ create form using our model """

    class Meta:
        model = SignUp
        fields = ['full_name', 'email']
        ## DEBUG ONLY ##  use this to manually add entries for different dates.
        # fields = ['full_name', 'email', 'created']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        user, domain = email.split('@')
        if not domain == 'mydomain.com':
            raise forms.ValidationError(
                "Please make sure you use your University email."
                )
        return email


class ContactForm(forms.Form):

    """ create form that will not be saved to our database """

    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
