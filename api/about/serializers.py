from rest_framework import serializers
from .models import AboutPage


class AboutPageSerializer(serializers.ModelSerializer):
    """
        Serializer for AboutPage model.
    """
    class Meta:
        model = AboutPage
        fields = '__all__'

    def validate_team_members(self, value):
        """
        Validate that team_members is a list of dictionaries with specific keys.
        """
        if not isinstance(value, list):
            raise serializers.ValidationError("Team members must be a list.")
        for member in value:
            if not isinstance(member, dict):
                raise serializers.ValidationError(f"Each team member must be a dictionary. Got: {member}.")
            if 'name' not in member or 'role' not in member:
                raise serializers.ValidationError("Each team member must have 'name' and 'role' keys.")
            if not isinstance(member['name'], str) or not isinstance(member['role'], str):
                raise serializers.ValidationError("Team member 'name' and 'role' must be strings.")
        return value

    def validate_contact_info(self, value):
        """
        Validate that contact_info is a dictionary with specific keys.
        """
        if not isinstance(value, dict):
            raise serializers.ValidationError("Contact info must be a dictionary.")
        for key in value.keys():
            if key not in ['email', 'phone', 'address']:
                raise serializers.ValidationError(f"Unexpected key {key} in contact info.")
            if not isinstance(value[key], str):
                raise serializers.ValidationError(f"Contact info '{key}' must be a string.")
        return value

    def validate_social_links(self, value):
        """
        Validate that social_links is a dictionary with specific keys.
        """
        if not isinstance(value, dict):
            raise serializers.ValidationError("Social links must be a dictionary.")
        for key in value.keys():
            if key not in ['facebook', 'twitter', 'linkedin', 'instagram']:
                raise serializers.ValidationError(f"Unexpected key {key} in social links.")
            if not isinstance(value[key], str):
                raise serializers.ValidationError(f"Social link '{key}' must be a string.")
        return value
