from django.core.files.uploadedfile import TemporaryUploadedFile
from drf_spectacular.utils import extend_schema_field
from drf_spectacular.types import OpenApiTypes
from rest_framework import serializers


@extend_schema_field(OpenApiTypes.BINARY)
class FileField(serializers.FileField):
    pass


class FileUploadSerializer(serializers.Serializer):
    file = FileField()
    file_import_format = serializers.ChoiceField(
       choices=[
           'json',
           # future formats can be added here
        ],
    )
    file_export_format = serializers.ChoiceField(
        choices=[
            'csv',
            # future formats can be added here
        ],
    )

    def validate(self, attrs):
        """
        Check that the uploaded import file request is a valid.
        """

        if 'file' not in attrs or attrs['file'] is None:
            raise serializers.ValidationError("No file uploaded.")

        if (
            'file_import_format' not in attrs
            or attrs['file_import_format'] is None
        ):
            raise serializers.ValidationError(
                "No file import format specified."
            )

        if (
            'file_export_format' not in attrs
            or attrs['file_export_format'] is None
        ):
            raise serializers.ValidationError(
                "No file export format specified."
            )

        if not isinstance(attrs['file'], TemporaryUploadedFile):
            raise serializers.ValidationError("Expected a file upload.")

        return attrs
