from django import forms
from article.models import Topic


class TopicForm(forms.Form):
    title = forms.CharField(max_length=150)
    subtitle = forms.CharField(max_length=100)
    text = forms.TextInput()
    url = forms.URLField()
    type = forms.ChoiceField(choices=Topic.TOPIC_TYPES)


class TopicModelForm(forms.ModelForm):
    class Meta:
        model = Topic
        exclude = ('author', 'creation_date')
