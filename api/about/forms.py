from django import forms
from .models import AboutPage


class AboutPageForm(forms.ModelForm):

    class Meta:
        model = AboutPage
        fields = [
            'mission_statement',
            'values',
            'history',
            'team_members',
            'contact_info',
            'social_links'
        ]
        widgets = {
            'mission_statement': forms.Textarea(
                attrs={
                    'rows': 5,
                    'placeholder': "Enter the mission statement."
                }),
            'values': forms.Textarea(
                attrs={
                    'rows': 5,
                    'placeholder': "Enter the values."
                }),
            'history': forms.Textarea(
                attrs={
                    'rows': 5,
                    'placeholder': "Enter the history."
                }),
            'team_members': forms.JSONField(
                attrs={
                    'placeholder': "Enter team members with details as a list of dictionaries"
                }),
            'contact_info': forms.JSONField(
                attrs={
                    'placeholder': "Enter contact info as a dictionary"
                }),
            'social_links': forms.JSONField(
                attrs={
                    'placeholder': "Enter social links as a dictionary"
                }),
        }

    def clean_team_members(self):
        """
            Validate that team_members is a list of dictionaries
            with name and role keys.
        """
        team_members = self.cleaned_data.get('team_members')

        if team_members:
            if not isinstance(team_members, list):
                raise forms.ValidationError("Team members must be a list.")

            for member in team_members:
                if not isinstance(member, dict):
                    raise forms.ValidationError(f"Each team member must be a dictionary. Got: {member}.")
                if 'name' not in member or 'role' not in member:
                    raise forms.ValidationError("Each team member must have 'name' and 'role' keys.")
                if not isinstance(member['name'], str) or not isinstance(member['role'], str):
                    raise forms.ValidationError("Team member 'name' and 'role' must be strings.")
        return team_members

    def clean_contact_info(self):
        """
            Validate that contact_info is a dictionary with specific keys.
        """
        contact_info = self.cleaned_data.get('contact_info')

        if contact_info:
            if not isinstance(contact_info, dict):
                raise forms.ValidationError("Contact info must be a dictionary.")
            for key in contact_info.keys():
                if key not in ['email', 'phone']:
                    raise forms.ValidationError(f"Unexpected key {key} in contact info.")
                if not isinstance(contact_info[key], str):
                    raise forms.ValidationError(f"Contact info '{key}' must be a string.")
        return contact_info

    def clean_social_links(self):
        """
            Validate that social_links is a dictionary with expected keys.
        """
        social_links = self.cleaned_data.get('social_links')

        if social_links:
            if not isinstance(social_links, dict):
                raise forms.ValidationError("Social links must be a dictionary.")
            for key in social_links.keys():
                if key not in ['linkedin', 'twitter', 'github', 'instagram']:
                    raise forms.ValidationError(f"Unexpected key {key} in social links.")
                if not isinstance(social_links[key], str):
                    raise forms.ValidationError(f"Social link '{key}' must be a string.")
        return social_links
