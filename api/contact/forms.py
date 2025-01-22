from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):

    """
        Form for users to contact through the website
    """

    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'subject', 'reason', 'message']
        widgets = {
            'message': forms.Textarea(attrs={
                'rows': 5,
                'placeholder': "Enter your message to us."}
            ),
            'reason': forms.Select(choices=ContactMessage.CONTACT_REASONS)
        }

    def clean_phone(self):
        """
            Validate phone nuber format
        """
        phone = self.cleaned_data.get('phone')

        if phone and not phone.isdigit():
            raise forms.ValidationError('Phone number should contain only digits.')
        return phone
