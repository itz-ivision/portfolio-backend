from rest_framework import serializers
from .models import BlogPost, BlogCategory, Tag


class CategorySerializer(serializers.ModelSerializer):
    """
        Serializer for the Category model
    """
    class Meta:
        model = BlogCategory
        fields = ['id', 'name', 'description']
        ref_name = 'BlogCategory'


class TagSerializer(serializers.ModelSerializer):
    """
        Serializer for Tag model
    """
    class Meta:
        model = Tag
        fields = ['id', 'name']


class BlogPostSerializer(serializers.ModelSerializer):
    """
        Serializer for the BlogPost model
    """
    tags = TagSerializer(many=True, read_only=True)
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = BlogPost
        fields = [
            'id',
            'title',
            'slug',
            'content',
            'excerpt',
            'author',
            'categories',
            'tags',
            'image',
            'published_date'
        ]

    def create(self, validated_data):
        """
            Override the create method to handle tag and category assignment.
        """
        tags_data = self.context['request'].data.get('tags', [])
        categories_data = self.context['request'].data.get('categories', [])
        blog_post = BlogPost.objects.create(**validated_data)

        for tag_id in tags_data:
            tag = Tag.objects.get(id=tag_id)
            blog_post.tags.add(tag)

        for cat_id in categories_data:
            cat = BlogCategory.objects.get(id=cat_id)
            blog_post.categories.add(cat)

        return blog_post

    def update(self, instance, validated_data):
        """
            Override the update method to handle tag and category assignment.
        """
        tags_data = self.context['request'].data.get('tags', [])
        categories_data = self.context['request'].data.get('categories', [])
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.title)
        instance.excerpt = validated_data.get('excerpt', instance.excerpt)
        instance.published_date = validated_data.get('published_date', instance.published_date)
        instance.save()

        instance.tags.clear()
        for tag_id in tags_data:
            tag = Tag.objects.get(id=tag_id)
            instance.tags.add(tag)

        instance.categories.clear()
        for cat_id in categories_data:
            cat = BlogCategory.objects.get(id=cat_id)
            instance.categories.add(cat)

        return instance
