from django.core.cache import cache

def get_data():
    data = cache.get('my_data')
    if not data:
        data = "Expensive Query Result"
        cache.set('my_data', data, timeout=60)
    return data
