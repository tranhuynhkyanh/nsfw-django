from django.urls import path
from apps.predict.views import PredictImageAPIView

urlpatterns = [
    path('/', PredictImageAPIView.as_view())
]
