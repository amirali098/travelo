from  django import forms
from blog.models import Comment,Newsletter
from captcha.fields import CaptchaField

class CommentForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Comment
        fields =['post','name','email','subject', 'message']



class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email']

