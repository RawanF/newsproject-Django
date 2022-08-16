from . import models
from django.views.generic.detail import DetailView
from django.views.generic import ListView, CreateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse_lazy


class ArticleListView(ListView):
    """
    a view for listing all articles
    """
    model = models.Article
    paginate_by = 10


class ArticleDetailView(DetailView):
    """
    a view for a single article detail
    """
    context_object_name = "article"
    model = models.Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["favorite"] = self.object.favorite_set.filter(
            user__id=self.request.user.id).first()
        return context


@method_decorator(login_required, name='dispatch')
class FavoriteListView(ListView):
    """
    a view for listing all favored articles by the current user
    """
    model = models.Favorite
    paginate_by = 9

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


@method_decorator(login_required, name='dispatch')
class FavoriteCreateView(CreateView):
    """
    a view to adding article to user favorite list
    """
    model = models.Favorite
    fields = ['user', 'article']

    def get_success_url(self):
        """
        override the function to add a success message
        and pass pk for the article detail page
        """
        messages.success(self.request, _('Added to favorite successfully!'))
        return reverse_lazy('article-detail',
                            kwargs={'pk': self.object.article.id})


@method_decorator(login_required, name='dispatch')
class FavoriteDeleteView(DeleteView):
    """
    a view to delete article from user favorite list
    """
    model = models.Favorite

    def get_success_url(self):
        """
        override the function to add a success message
        and pass pk for the article detail page
        """
        messages.success(self.request, _(
            'Removed from favorite successfully!'))
        return reverse_lazy('article-detail',
                            kwargs={'pk': self.object.article.id})
