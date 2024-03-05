from django.urls import path
from hexlet_django_blog.article.views import IndexView, ArticleView, ArticleCommentsView
from hexlet_django_blog.article import views

urlpatterns = [
    path('', IndexView.as_view()),
    path('<int:id>/', ArticleView.as_view(), name='article_detail'),
    path('<int:article_id>/comments/<int:id>/', ArticleCommentsView.as_view()),
]
