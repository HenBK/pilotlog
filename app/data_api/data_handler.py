import json

from data_api.data_importer import DataImporter
from data_api.data_exporter import DataExporter
from data_api.data_mapper import DataMapper
from data_api.exceptions import BadFileError


class DataHandler:
    """
    DataHandler class is responsible for orquestrating data import and export
    """

    ALLOWED_IMPORT_FILE_FORMATS = [
        'json',
    ]

    ALLOWED_EXPORT_FILE_FORMATS = [
        'csv',
    ]

    def __init__(self, import_format='json', export_format='csv'):
        self.import_format = import_format
        self.export_format = export_format

    def process_data(self, data_source):
        """
        Process data from data source and return it in the specified format
        """
        parsed_data = self._parse_data_source(
            file_format=self.import_format,
            data_source=data_source,
        )
        imported_data = self._import_data(parsed_data)
        exported_data = self._export_data(imported_data)

        return exported_data

    def _import_data(self, data_source):
        """Import data from data source persisting it in the database"""
        data_mapper = DataMapper()

        data_importer = DataImporter(
            data_source=data_source,
            data_mapper=data_mapper,
        )

        return data_importer.import_data()

    def _export_data(self, data_source):
        """Export data to a file"""
        if self.export_format not in self.ALLOWED_EXPORT_FILE_FORMATS:
            raise ValueError("Invalid export file format has been set.")

        data_exporter = DataExporter(file_format=self.export_format)
        exported_data = data_exporter.export_data(data_source=data_source)
        return exported_data

    def _parse_data_source(self, data_source, file_format='json'):
        """
        Parse data source based on the specified format
        """

        if file_format not in self.ALLOWED_IMPORT_FILE_FORMATS:
            raise ValueError("Invalid file format.")

        if file_format == 'json':
            # Load the file and try to parse it as JSON
            try:
                parsed_data = json.load(data_source)
            except json.JSONDecodeError:
                raise BadFileError("Invalid JSON file.")

        return parsed_data
