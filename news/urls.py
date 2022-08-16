
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleListView.as_view(), name="article-list"),
    path('<int:pk>/', views.ArticleDetailView.as_view(),
         name="article-detail"),
    path('favorites/create', views.FavoriteCreateView.as_view(),
         name="favorite-create"),
    path('favorites/<int:pk>/delete',
         views.FavoriteDeleteView.as_view(), name="favorite-delete"),
    path('favorites/', views.FavoriteListView.as_view(), name="favorite-list"),
]
