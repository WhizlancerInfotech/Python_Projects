from django.http import JsonResponse
import asyncio

async def async_view(request):
    await asyncio.sleep(2)
    return JsonResponse({"message": "Async response"})
