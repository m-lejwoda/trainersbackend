from django import forms
from tinymce.widgets import TinyMCE
from .models import Post,Event


# class TinyMCEWidget(TinyMCE):
#     def use_required_attribute(self, *args):
#         return False


class PostForm(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCE(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )
    class Meta:
        model = Post
        fields = '__all__'

class DateInput(forms.DateInput):
    input_type = 'date'

class TrainerEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['date','start_hour','end_hour','client_name','client_email','client_phone','trainer']
        widgets = {
            'date': DateInput(),
        }