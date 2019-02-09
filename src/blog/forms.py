from django import forms
from .models import UserReview,Review
class userReviewForm(forms.Form):
    name = forms.CharField()
    comment = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
    rk = forms.CharField(widget=forms.HiddenInput())

    def save(self):
        x = self.cleaned_data.get('name')
        y = self.cleaned_data.get('email')
        w = self.cleaned_data.get('comment')
        k = self.cleaned_data.get('rk')
        print(self)
        print(k)
        r = Review.objects.get(pk=k)
        review = UserReview(name=x,email=y,comment=w,review=r)
        review.save()
		# return photo


    