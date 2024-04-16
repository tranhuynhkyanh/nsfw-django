from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView

from apps.predict import predict
from core.settings import CREDENTIAL, MODEL
from ultis.api_helper import api_decorator


# Create your views here.
class PredictImageAPIView(APIView):
    @api_decorator
    def post(self, request):
        token = request.query_params.get('key')
        if token != CREDENTIAL:
            return {}, "Key không hợp lệ", status.HTTP_400_BAD_REQUEST

        image = request.data.get('image', None)
        if not image:
            return {}, "Không có ảnh", status.HTTP_204_NO_CONTENT

        predict.classify(MODEL, image.temporary_file_path())
        print(predict)

        return predict,"Kết quả", status.HTTP_200_OK

