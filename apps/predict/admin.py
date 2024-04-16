from django.contrib import admin

from apps.predict.models import HistoryPredict


# Register your models here.
@admin.register(HistoryPredict)
class PredictAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'result', 'created_at')
    ordering = ('-created_at',)

    list_per_page = 10
