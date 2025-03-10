from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .utils import get_groq_response


def chat_view(request):
    return render(request, "app/chat.html")


@csrf_exempt
def chat_api(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_input = data.get("message", "").strip()
            if user_input:
                bot_response = get_groq_response(user_input)
                return JsonResponse({"response": bot_response})
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

    return JsonResponse({"error": "Invalid request"}, status=400)
