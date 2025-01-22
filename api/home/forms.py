from django import forms
from .models import HomePage


class HomePageForm(forms.ModelForm):

    class Meta:
        model = HomePage
        fields = [
            'introduction',
            'header_title',
            'header_subtitle',
            'summary',
            'professional_summary',
            'call_to_action',
            'contact_info',
            'social_links'
        ]
        widgets = {
            'introduction': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Enter introduction'}),
            'header_title': forms.TextInput(attrs={'placeholder': 'Enter header title'}),
            'header_subtitle': forms.TextInput(attrs={'placeholder': 'Enter header subtitle'}),
            'summary': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Enter summary'}),
            'professional_summary': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Enter professional summary'}),
            'call_to_action': forms.URLInput(attrs={'placeholder': 'Enter call to action URL'}),
            'contact_info': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Enter contact info as a dictionary'}),
            'social_links': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Enter social links as a dictionary'})
        }

    def clean_contact_info(self):

        contact_info = self.cleaned_data.get('contact_info')

        if contact_info:
            if not isinstance(contact_info, dict):
                return forms.ValidationError("Contact Info Must be a dictionary")
            for key in contact_info.keys():
                if key not in ['email', 'phone']:
                    raise forms.ValidationError(f"Unexpected key {key} in contact info.")
        return contact_info

    def clean_social_links(self):

        social_links = self.cleaned_data.get('social_links')

        if social_links:
            if not isinstance(social_links, dict):
                raise forms.ValidationError("Social links must be a dictionary.")
            required_keys = ['linkedin', 'twitter', 'github', 'instagram']
            for key in required_keys:
                if key not in social_links:
                    raise forms.ValidationError(f"Missing required social link key: {key}")
                if not isinstance(social_links[key], str):
                    raise forms.ValidationError(f"Social link '{key}' must be a string.")

        return social_links
