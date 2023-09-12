from django import forms

from .models import Note


class PostForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('text', 'time',)
        labels = {
            'text': 'Какую задачу решить?',
            'time': 'И когда же она нам нужна?',
        }