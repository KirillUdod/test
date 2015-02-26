from django.shortcuts import render, render_to_response, redirect
from django.http.response import HttpResponse, Http404, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from article.models import Article, Comments, likes_table
from django.core.exceptions import ObjectDoesNotExist
from django.core.context_processors import csrf
from article.forms import CommentForm, ArticleADDForm
from django.contrib import auth
from django.core.paginator import Paginator
from django.contrib.auth.models import User

# Create your views here.
    
def articles(request, page_number=1):
    all_articles = Article.objects.all().order_by('-article_date')
    current_page = Paginator(all_articles, 3)
    
    args = {}
    args.update(csrf(request))
    args['articles'] = current_page.page(page_number)
    args['username'] = auth.get_user(request).username
    return render_to_response('articles.html', args)
    
def article(request, article_id=1, comments_page_number=1):
    comment_form = CommentForm
    args = {}
    args.update(csrf(request))                         
    args['article'] = Article.objects.get(id=article_id)
    all_comments = Comments.objects.filter(comments_article_id = article_id)
    current_page_com = Paginator(all_comments, 3)
    args['comments'] = current_page_com.page(comments_page_number)
    args['form'] = comment_form
    args['username'] = auth.get_user(request).username
    args['article_id'] = article_id
    return render_to_response('article.html', args)
                                                             
def auth_required(function):
    def check_auth(request, article_id=1):
        if not request.user.is_authenticated():
            response = redirect('/auth/login/')
            back_url = request.META['HTTP_REFERER']
            response.set_cookie('last_article', back_url)
            return response
        return function(request, article_id)
    return check_auth

@auth_required
def addlike(request, article_id):
    back_url = request.META['HTTP_REFERER']
    try:
        if likes_table.objects.filter(likes_from=request.user.id, likes_for = article_id):
            exit
        else:
            like = likes_table(likes_from = request.user.id, likes_for = article_id)
            like.save()
            article = Article.objects.get(id=article_id)
            likes = len(likes_table.objects.filter(likes_for = article_id))
            article.article_likes = likes
            article.save()
            return redirect(back_url)
    except ObjectDoesNotExist:
        raise Http404
    return redirect(back_url)

@auth_required
def addcomment(request, article_id):
#    if request.POST and ('pause_com' not in request.session):
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.comments_article = Article.objects.get(id=article_id)
        comment.comments_from = request.user
        form.save()
#            request.session.set_expiry(60)
#            request.session['pause_com'] = True
    return redirect('/articles/get/%s/' % article_id )
    
@auth_required    
def addarticle(request , article_id):
    if request.POST:
        form = ArticleADDForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    art_form = ArticleADDForm
    args = {}
    args.update(csrf(request))
    args['form'] = art_form
#    request.session.set_expiry(60)
#    request.session['pause_post'] = True
    return render_to_response('create_article.html', args)
    
def search_title(request):
    if request.method == "POST":
        search_text = request.POST['search_text']
    else:
        search_text = ''
        
    articles = Article.objects.filter(article_title__contains=search_text)
    
    return render_to_response('ajax_search.html', {'articles': articles})
    
