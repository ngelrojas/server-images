from django.urls import path
from .views import UploadViewSet

app_name = "uploaded-images"

urlpatterns = [
    path(
        "images", UploadViewSet.as_view({"post": "create"}), name="create-upload-images"
    )
]
