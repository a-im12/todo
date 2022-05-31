from django.forms import ModelForm
from .models import TodoPost

class TodoPostForm(ModelForm):
    class Meta:
        model = TodoPost
        fields = ['todo']