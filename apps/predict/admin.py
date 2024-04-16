from django.contrib import admin


# Register your models here.
class PredictAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'result', 'created_at')
    ordering = ('-created_at',)

    list_per_page = 10