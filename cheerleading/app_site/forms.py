from django import forms
from app_site.models import Feedback


class FeedbackForm(forms.ModelForm):
    # name = forms.CharField(required=True, max_length=100, help_text='Имя')
    # tel = forms.CharField(required=True, max_length=20)
    # email = forms.EmailField(required=True)
    # message = forms.Textarea()
    # create_at = forms.DateTimeField()


    class Meta:
        model = Feedback
        fields = ('name', 'tel', 'email', 'message',)