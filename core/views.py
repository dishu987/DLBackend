from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import base64
from .DLModel.main import blur_image_and_encode



class TestAPIView(APIView):
    def get(self, request, format=None):
        return Response({"data":"This is test"}, status=status.HTTP_200_OK)
    def post(self, request, format=None):
        # Check if the request contains an image
        if 'image' in request.FILES:
            image_file = request.FILES['image']
            radius = request.POST['radius']
            if radius:
                image_data = image_file.read()
                x = blur_image_and_encode(image_data,radius)
                return Response({"image_data": x}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "No image found in the request"}, status=status.HTTP_400_BAD_REQUEST)
