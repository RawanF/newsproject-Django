from django.db import models
from django.utils.translation import ugettext_lazy as _
from accounts.models import User


class Article(models.Model):
    title = models.CharField(_('title'), max_length=225, null=False)
    source_id = models.CharField(
        _('source id'), max_length=200, blank=True, null=True)
    source_name = models.CharField(
        _('source name'), max_length=200, blank=True, null=True)
    author = models.CharField(
        _('author'), max_length=200, blank=True, null=True)
    description = models.TextField(_('description'), blank=True, null=True)
    url = models.URLField(_('url'), blank=True, null=True)
    url_to_image = models.URLField(_('url to image'), blank=True, null=True)
    published_at = models.DateTimeField(
        _('published at'), blank=True, null=True)
    content = models.TextField(_('content'), blank=True, null=True)


class Favorite(models.Model):
    """
    a model for the favorited articles by user
    which is equivalent to ManytoMany field
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('user', 'article'))
