from django.shortcuts import render
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.core.files.storage import FileSystemStorage
from .serializers import UploadSerializer


class UploadViewSet(ViewSet):
    """view to manage images"""

    serializer_class = UploadSerializer

    def list(self, request):
        """list images uploaded"""
        return Response("get api list")

    def create(self, request):
        try:
            file_uploaded = request.FILES.get("file_uploaded")
            f_s = FileSystemStorage()
            filename = f_s.save(file_uploaded.name, file_uploaded)
            image_url = f_s.url(filename)

            return Response({"data": f"{image_url}"}, status=status.HTTP_201_CREATED)
        except Exception as err:
            return Response(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_404_NOT_FOUND
            )
