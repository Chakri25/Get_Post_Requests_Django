from django import forms

class toDoListForm(forms.Form):
	data = forms.CharField(label='',max_length = 20)