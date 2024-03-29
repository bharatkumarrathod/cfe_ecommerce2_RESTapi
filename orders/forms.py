from django import forms
from django.contrib.auth import get_user_model
from .models import UserAddress

user = get_user_model()


class GuestCheckoutForm(forms.Form):
    email = forms.EmailField()
    email2 = forms.EmailField(label="Verify Email")

    def clean_email2(self):
        email = self.cleaned_data.get("email")
        email2 = self.cleaned_data.get("email2")

        if email == email2:
            user_exists = user.objects.filter(email=email).count()
            if user_exists:
                raise forms.ValidationError("This user already exists. Please login instead.")
            return email2
        else:
            raise forms.ValidationError("Please confirm emails are the same")


class AddressForm(forms.Form):
    billing_address = forms.ModelChoiceField(
        queryset=UserAddress.objects.filter(type="billing"),
        empty_label=None,
        widget=forms.RadioSelect
    )
    shipping_address = forms.ModelChoiceField(
        queryset=UserAddress.objects.filter(type="shipping"),
        empty_label=None,
        widget=forms.RadioSelect
    )


class UserAddressForm(forms.ModelForm):
    class Meta:
        model = UserAddress
        fields = [
            'street',
            'city',
            'county',
            'postcode',
            'type'
        ]
