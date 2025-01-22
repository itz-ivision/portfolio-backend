from rest_framework import serializers
from .models import ContactMessage


class ContactMessageSerializer(serializers.ModelSerializer):
    """
        Serializer for ContactMessage model.
    """
    class Meta:
        model = ContactMessage
        fields = ['id', 'name', 'email', 'phone', 'subject', 'reason', 'message', 'sent_at', 'read']
        read_only_fields = ['sent_at', 'read']

    @staticmethod
    def validate_phone(value):
        """
            Validate User Phone number Input
        """
        if value and not  value.isdigit():
            raise serializers.ValidationError('Phone number should contain digits only.')
        return value

    def create(self, validated_data):
        """
            Create and return a new `ContactMessage` instance, given the validated data.
        """
        return ContactMessage.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
            Update and return an existing `ContactMessage` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.subject = validated_data.get('subject', instance.subject)
        instance.reason = validated_data.get('reason', instance.reason)
        instance.message = validated_data.get('message', instance.message)
        instance.read = validated_data.get('read', instance.read)
        instance.save()
        return instance
