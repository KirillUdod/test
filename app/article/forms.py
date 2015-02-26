from django.forms import ModelForm
from article.models import Comments, Article
    
class CommentForm(ModelForm):
    class Meta():
        model = Comments
        fields = ['comments_text']
        
class ArticleADDForm(ModelForm):
    class Meta():
        model = Article
        fields = [ 'article_title',    'article_text', 'thubnail']
        

