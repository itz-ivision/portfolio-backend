from django import forms
from .models import Category, BlogPost, Tag


class BlogPostForm(forms.ModelForm):
    """
        Form for creating and updating BlogPost instances.
    """
    class Meta:
        model = BlogPost
        fields = [
            'title',
            'slug',
            'content',
            'excerpt',
            'author',
            'categories',
            'tags',
            'images',
            'published_date',
        ]
        widgets = {
            'content': forms.Textarea(attrs={'rows': 10, 'placeholder': 'Enter blog content'}),
            'excerpt': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Enter a short excerpt'}),
            'categories': forms.CheckboxSelectMultiple(),
            'tags': forms.CheckboxSelectMultiple(),
            'image': forms.ClearableFileInput(attrs={'multiple': False}),
        }

    def __init__(self, *args, **kwargs):
        """
            Initialize the form and populate the categories and tags fields.
        """
        super().__init__(*args, **kwargs)
        self.fields['categories'].queryset = Category.objects.all()
        self.fields['tags'].queryset = Tag.objects.all()
