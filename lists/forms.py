from django import forms


class ItemForm(forms.Form):
    """Form element of list"""
    item_text = forms.CharField(
        widget=forms.fields.TextInput(
            attrs={
                'placeholder': 'Enter a to-do item',
            }
        ),
    )
