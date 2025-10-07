from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .predictors.pipeline import PredictionPipeline
from users.models import User
from .predictors.selection_tree import SELECTION_TREE, FEATURE_CONFIG_MAP, get_unlocked_features
from .predictors.utils import merge_dicts

class AddFeatureView(APIView):
    def post(self, request):
        guid = request.COOKIES.get('user_guid')
        if not guid:
            return Response({'error': 'User GUID cookie not found'}, status=400)
        
        user = get_object_or_404(User, guid=guid)
        feature_id = request.data.get("feature_id")
        if not feature_id or feature_id not in FEATURE_CONFIG_MAP:
            return Response({'error': 'Invalid or missing feature_id'}, status=400)
        
        feature_config = FEATURE_CONFIG_MAP[feature_id]
        updated_config = merge_dicts(user.model_config or {}, feature_config)
        user.model_config = updated_config
        selected = user.model_config.get("selected_features", [])
        if feature_id not in selected:
            selected.append(feature_id)
        user.model_config["selected_features"] = selected
        user.save()

        pretrained_model = request.data.get('model')
        pipeline = PredictionPipeline(config=updated_config, pretrained_model=pretrained_model)
        model_json = pipeline.get_model()

        return Response({'model': model_json})
    

class AvailableFeaturesView(APIView):
    def get(self, request):
        guid = request.COOKIES.get("user_guid")
        if not guid:
            return Response({"error": "User GUID cookie not found"}, status=400)
        
        user = get_object_or_404(User, guid=guid)
        selected = user.model_config.get("selected_features", [])
        unlocked = get_unlocked_features(selected)
        
        # Optionally include labels or config deltas
        features = [{"id": f, "label": f.capitalize()} for f in unlocked]
        return Response({"features": features})



class TrainView(APIView):
    def post(self, request):
        guid = request.COOKIES.get('user_guid')
        if not guid:
            return Response({'error': 'User GUID cookie not found'}, status=400)
        
        user = get_object_or_404(User, guid=guid)
        config = user.model_config or {}
        
        pretrained_model = request.data.get('model')

        pipeline = PredictionPipeline(config=config, pretrained_model=pretrained_model)
        model_json = pipeline.get_model()

        return Response({'model': model_json})

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

        pretrained_model = request.data.get('model')
        
        pipeline = PredictionPipeline(config=config, pretrained_model=pretrained_model)
        prediction = pipeline.predict(prompt)
        model_json = pipeline.get_model()
        return Response({'prediction': prediction, 'model': model_json})