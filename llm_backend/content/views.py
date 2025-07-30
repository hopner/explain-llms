from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Chapter
from markdown import markdown

class ChapterView(APIView):
    def get(self, request, slug):
        lang = request.query_params.get('lang', 'en')
        chapter = Chapter.objects.get(slug=slug)
        sections = chapter.sections.filter(language=lang).order_by('order')
        return Response({
            "title": chapter.title,
            "sections": [
                {
                    "content": markdown(s.content_markdown),
                    "animation_state": s.animation_state
                } for s in sections
            ]
        })
    