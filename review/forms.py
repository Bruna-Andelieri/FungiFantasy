from django import forms


class ReviewForm(forms.Form):
    title = forms.CharField(max_length=200)
    rating = forms.IntegerField(min_value=1, max_value=5)
    text = forms.CharField(widget=forms.Textarea)