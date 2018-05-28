from django import forms 

from .models import Post

class PostForm(forms.ModelForm):
	"""docstring for PostForm"""
	class Meta(object):
		model = Post
		fields = ('title', 'text',)
		