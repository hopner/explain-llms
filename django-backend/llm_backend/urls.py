"""
URL configuration for llm_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from text_generation.views import (PredictView, 
                                   AddFeatureView, 
                                   RemoveFeatureView, 
                                   AvailableFeaturesView, 
                                   TrainView, 
                                   SkillTreeView,
                                   TokenizeView,
                                   BooksDatasetView,
                                   SetCorpusView)
from users.views import UserCreateView, UserConfigView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/predict/', PredictView.as_view()),
    path('api/users/', UserCreateView.as_view()),
    path('api/users/<str:guid>/config/', UserConfigView.as_view()),
    path('api/add-feature/', AddFeatureView.as_view()),
    path('api/remove-feature/', RemoveFeatureView.as_view()),
    path('api/available-features/', AvailableFeaturesView.as_view()),
    path('api/skill-tree/', SkillTreeView.as_view()),
    path('api/train/', TrainView.as_view()),
    path('api/tokenize/', TokenizeView.as_view()),
    path('api/books-dataset/', BooksDatasetView.as_view()),
    path('api/set-corpus/', SetCorpusView.as_view()),
]
