from django.urls import path
from .views import (
    ArticleCreateView,
    ArticleUpdateView,
    ArticleListView,
    ArticleDeleteView,
    ArticleDetailView
)

app_name = "blog"

urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('create/', ArticleCreateView.as_view(), name='article-create'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('<int:id>/update/', ArticleUpdateView.as_view(), name='article-update'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article-delete'),
    # path('', article_list_view, name='article-list'),
    # path('<int:id>/', article_detail_view, name='article-detail'),
]
