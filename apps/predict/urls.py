from django.urls import path
from apps.predict.views import PredictImageAPIView

urlpatterns = [
    path('nsfw/', PredictImageAPIView.as_view())
]
