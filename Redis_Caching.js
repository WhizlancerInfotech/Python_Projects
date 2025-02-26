from django.core.cache import cache
from django.http import JsonResponse

def cached_view(request):
    data = cache.get("cached_data")
    if not data:
        data = {"message": "Data fetched from DB"}
        cache.set("cached_data", data, timeout=60)  # Cache for 60 seconds
    return JsonResponse(data)
