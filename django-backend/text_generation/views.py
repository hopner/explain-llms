from rest_framework.views import APIView
from rest_framework.response import Response

class PredictView(APIView):
    def post(self, request):
        prompt = request.data.get('prompt', '')
        if not prompt:
            return Response({'error': 'No prompt provided'}, status=400)
        
        prediction = "This is a mock prediction for: " + prompt
        
        return Response({'prediction': prediction})