from django import forms


class ProjectCreateForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField(max_length=254)
    countUser = forms.IntegerField()


class ProjectFilterForm(forms.Form):
    title = forms.CharField(max_length=100)
    countUser = forms.IntegerField()
