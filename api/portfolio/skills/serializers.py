from rest_framework import serializers
from .models import SkillsCategory, Skills


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = ['id', 'name', 'proficiency', 'category', 'description']


class CategorySerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True)

    class Meta:
        model = SkillsCategory
        fields = ['id', 'name', 'description', 'skills']
        ref_name = 'SkillsCategory'
