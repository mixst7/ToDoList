from django import forms

class Todoform(forms.Form):
    text = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class' : 'form-control',
                                                                         'placeholder' : 'Enter todo delete',
                                                                         'area-label': 'Todo',
                                                                         'area describedby' : 'add-btn'
                                                                         }))

