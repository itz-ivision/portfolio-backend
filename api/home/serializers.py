from rest_framework import serializers
from .models import HomePage


class HomePageSerializer(serializers.ModelSerializer):

    class Meta:
        model = HomePage
        fields = "__all__"

    # def create(self, validated_data):
    #     """
    #     Create and return a new `HomePage` instance, given the validated data.
    #     """
    #     return HomePage.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `HomePage` instance, given the validated data.
    #     """
    #     for attr, value in validated_data.items():
    #         setattr(instance, attr, value)
    #     instance.save()
    #     return instance

