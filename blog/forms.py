
from django import forms
from .models import BlogPost, Comment, Category




class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title','content','logo_img','category','status')
    status = forms.ChoiceField(choices=BlogPost.status_CHOICES)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Select")    


     
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)