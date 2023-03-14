from django import forms


class WordForm(forms.Form):
    parameter_word = forms.CharField(label='Анализ үчүн сөз жазыңыз...', max_length=255)


class TextFileForm(forms.Form):
    text = forms.CharField(label='Enter Text', widget=forms.Textarea(attrs={'class': 'form-control'}), required=False)
    file = forms.FileField(label='Upload File', required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class': 'form-control'})
        self.fields['file'].widget.attrs.update({'class': 'form-control'})

    def clean(self):
        cleaned_data = super().clean()
        if not cleaned_data.get('text') and not cleaned_data.get('file'):
            raise forms.ValidationError('Please enter text or upload a file')


