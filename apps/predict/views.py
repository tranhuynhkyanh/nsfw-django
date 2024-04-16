import os
import tempfile

from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from apps.predict import predict
from apps.predict.models import HistoryPredict
from core.settings import CREDENTIAL, MODEL
from ultis.api_helper import api_decorator


# Create your views here.
class PredictImageAPIView(APIView):
    permission_classes = [AllowAny, ]

    @api_decorator
    def post(self, request):
        token = request.data.get('key')
        if token != str(CREDENTIAL):
            return {}, "Key không hợp lệ", status.HTTP_400_BAD_REQUEST

        image = request.data.get('image', None)
        if not image:
            return {}, "Không có ảnh", status.HTTP_204_NO_CONTENT
        # Tạo một tệp tạm thời từ dữ liệu hình ảnh
        with tempfile.NamedTemporaryFile(delete=False) as temp_image:
            temp_image.write(image.read())
            temp_image_path = temp_image.name

        rslt = predict.classify(MODEL, temp_image_path)
        pre = HistoryPredict.objects.create(image=image,
                                            result=rslt)

        # Sau khi sử dụng, xóa tệp tạm thời
        os.unlink(temp_image_path)

        return rslt, "Kết quả", status.HTTP_200_OK
