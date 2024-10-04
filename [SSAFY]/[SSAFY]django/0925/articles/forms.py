from django import forms
from .models import Article
class ArticleForm(forms.ModelForm):
    # author = forms.CharField(
    #     widget=forms.Select(
    #         choices=[('SSS', '트리플S'), ('a', 'A급'), ('f', '쓰레기')] #value, represent
    #     )
    # )
    # is_adult = forms.BooleanField(
    #     widget=forms.RadioSelect(
    #         choices=[(False, '미성년자'), (True, '19금')]
    #     )
    # )


    class Meta:
        model = Article
        fields = '__all__'