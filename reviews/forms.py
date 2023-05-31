from django import forms
from .models import Review

# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label='Your name', max_length=100, error_messages={
#         'required': 'Your name must not be empty',
#         'max_length': 'Please enter a shorter name'
#     })
#     review_text = forms.CharField(label='Your Feedback', widget=forms.Textarea, max_length=200)
#     rating = forms.IntegerField(label='Your Rating', min_value=1, max_value=5)

class ReviewForm(forms.ModelForm):
    class Meta():
        model = Review
        fields = '__all__' # Want to add specific fields add them in a list like [user_name, rating]
        # exclude = ['review_text'] exclude specific field and include all other
        labels = {
            'user_name': 'Your Name',
            'review_text': 'Your Feedback',
            'rating': 'Your Rating',
            'agreed_to_submit': 'Agree on the above submission'
        }
        error_messages = {
            'user_name': {
                'required': 'Your name must not be empty',
                'max_length': 'Please enter a shorter name'
            }
        }