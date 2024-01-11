from django.http import FileResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser

from data_api.data_handler import DataHandler
from data_api.serializers import FileUploadSerializer
from data_api.exceptions import BadFileError


class ImportDataView(APIView):
    parser_classes = [MultiPartParser]
    serializer_class = FileUploadSerializer

    def post(self, request, format=None):
        """
        Receives an import file and returns a processed
        version of the imported data
        """

        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

        file_data = serializer.validated_data['file']
        import_format = serializer.validated_data['file_import_format']
        export_format = serializer.validated_data['file_export_format']

        data_handler = DataHandler(
            import_format=import_format,
            export_format=export_format,
        )

        try:
            processed_export_file = data_handler.process_data(file_data)
        except BadFileError:
            return Response(
                {
                    'error': 'Invalid file format.',
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        except Exception:
            return Response(
                {
                    'error': 'An error occurred while processing the file.',
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        return FileResponse(
            processed_export_file,
            as_attachment=True,
            filename=f'export_file.{export_format}',
        )
