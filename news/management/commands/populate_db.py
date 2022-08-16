from django.core.management.base import BaseCommand
from news.models import Article
import requests
import json


class Command(BaseCommand):
    help = 'Create an Article from API'

    def handle(self, *args, **options):
        url = "https://newsapi.org/v2/everything?q=Apple&apiKey=fc5b72bf95db4fa1b2f553f503398b04"
        response = requests.get(url)
        articles = response.json
        response = json.loads(response.text)
        articles = response['articles']
        print(articles)

        for a in articles:
            article = Article.objects.create()
            article.source_id = a['source']['id']
            article.source_name = a['source']['name']
            article.author = a['author']
            article.title = a['title']
            article.description = a['description']
            article.url = a['url']
            article.url_to_image = a['urlToImage']
            article.published_at = a['publishedAt']
            article.content = a['content']
            article.save()

        self.stdout.write(self.style.SUCCESS('Successfully created articles'))
