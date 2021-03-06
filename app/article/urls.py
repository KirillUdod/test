from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^all/$', 'article.views.articles'),
    url(r'^get/(?P<article_id>\d+)/$', 'article.views.article'),
    url(r'^get/(?P<article_id>\d+)/(?P<comments_page_number>\d+)/$', 'article.views.article'),
    url(r'^addlike/(?P<article_id>\d+)/$', 'article.views.addlike'),
    url(r'^addcomment/(?P<article_id>\d+)/$', 'article.views.addcomment'),
    url(r'^create/$', 'article.views.addarticle'),
    url(r'^page/(\d+)/$', 'article.views.articles'),
    url(r'^search/', 'article.views.search_title'),
    url(r'^$', 'article.views.articles'),
)
