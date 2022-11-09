from django import forms


class ItemForm(forms.Form):
    """Form element of list"""
    item_text = forms.CharField()