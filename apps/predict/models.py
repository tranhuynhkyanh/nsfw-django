import uuid

from django.db import models


# Create your models here.
class HistoryPredict(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    image = models.ImageField(upload_to='assets/predict')
    result = models.JSONField(default=dict)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
