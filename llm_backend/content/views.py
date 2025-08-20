from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Chapter
from markdown import markdown

class ChapterView(APIView):
    def get(self, request, slug):
        lang = request.query_params.get('lang', 'en')
        chapter = get_object_or_404(Chapter, slug=slug)
        sections = chapter.sections.filter(language=lang).order_by('order')
        return Response({
            "title": chapter.title,
            "sections": [
                {
                    "order": s.order,
                    "content_markdown": s.content_markdown,
                    "content_html": markdown(s.content_markdown),
                    "animation_state": s.animation_state
                } for s in sections
            ]
        })
    
class PredictView(APIView):
    def post(self, request):
        prompt = request.data.get('prompt', '')
        if not prompt:
            return Response({'error': 'No prompt provided'}, status=400)
        
        prediction = "This is a mock prediction for: " + prompt
        
        return Response({'prediction': prediction})