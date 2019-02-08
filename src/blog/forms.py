from django import forms

class userReviewForm(forms.Form):
    name = forms.CharField()
    comment = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()


    