from rest_framework.serializers import Serializer, FileField


class UploadSerializer(Serializer):
    """serialzer to upload files"""

    file_uploaded = FileField()

    class Meta:
        fields = ["file_uploaded"]
