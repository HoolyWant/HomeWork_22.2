from django.core.cache import cache

from config import settings
from shop.models import Product


def get_categories():
    if settings.CACHE_ENABLED:
        key = 'categories'
        categories = cache.get(key)
        if categories is None:
            categories = Category.objects.all()
            cache.set(key, categories)
        else:
            categories = Category.objects.all()

        return categories



