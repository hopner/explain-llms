from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .predictors.pipeline import PredictionPipeline
from users.models import User

class PredictView(APIView):
    def post(self, request):
        prompt = request.data.get('prompt', '')
        if not prompt:
            return Response({'error': 'No prompt provided'}, status=400)
        
        guid = request.COOKIES.get('user_guid')
        if not guid:
            return Response({'error': 'User GUID cookie not found'}, status=400)
        
        user = get_object_or_404(User, guid=guid)
        config = user.model_config or {}
        
        pipeline = PredictionPipeline(config=config)
        prediction = pipeline.predict(prompt)
        return Response({'prediction': prediction})