from django.http import JsonResponse
from transformers import pipeline
from django.views.decorators.csrf import csrf_exempt

import json

# Initialize the Hugging Face pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

@csrf_exempt  # Disable CSRF for this view
def analyze_sentiment(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        text = data.get('text', '')
        
        if text:
            result = sentiment_pipeline(text)
            return JsonResponse(result, safe=False)
        else:
            return JsonResponse({"error": "No text provided"}, status=400)

    return JsonResponse({"error": "Method not allowed"}, status=405)
