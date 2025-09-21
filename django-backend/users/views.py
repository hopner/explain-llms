from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
import uuid

class UserCreateView(APIView):
    def post(self, request):
        guid = request.data.get('guid')
        
        if not guid:
            return Response({'error': 'GUID required'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            uuid_obj = uuid.UUID(guid)
        except ValueError:
            return Response({'error': 'Invalid GUID format'}, status=status.HTTP_400_BAD_REQUEST)
        
        user, created = User.objects.get_or_create(guid=uuid_obj)
        
        return Response({
            'guid': str(user.guid),
            'created': created,
            'created_at': user.created_at
        })

class UserConfigView(APIView):
    def put(self, request, guid):
        try:
            uuid_obj = uuid.UUID(guid)
            user = User.objects.get(guid=uuid_obj)
        except (ValueError, User.DoesNotExist):
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
        config = request.data.get('config', {})
        user.model_config = config
        user.save()
        
        return Response({'message': 'Config updated successfully'})
    
    def get(self, request, guid):
        try:
            uuid_obj = uuid.UUID(guid)
            user = User.objects.get(guid=uuid_obj)
        except (ValueError, User.DoesNotExist):
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
        return Response({
            'guid': str(user.guid),
            'config': user.model_config,
            'created_at': user.created_at,
            'updated_at': user.updated_at
        })