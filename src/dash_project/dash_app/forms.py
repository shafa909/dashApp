from django import forms

class HomeForm(forms.Form):
	Query = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 2}))
