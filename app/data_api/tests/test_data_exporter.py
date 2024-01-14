import io

from data_api.data_exporter import (
    DataExporter,
)


class TestDataExporter:

    def test_export_data(self):
        """
        Test export data to csv file.
        """

        data_exporter = DataExporter(
            file_format='csv',
        )

        data_source = [
            {
                'id': 1,
                'name': 'Test',
            },
            {
                'id': 2,
                'name': 'Test2',
            }
        ]

        file = data_exporter.export_data(data_source)

        assert file is not None
        assert isinstance(file, io.BytesIO)
        assert file.getvalue() == b'id,name\r\n1,Test\r\n2,Test2\r\n'

    def test_export_data_invalid_file_format(self):
        """
        Test export data to invalid file format raises exception.
        """

        data_exporter = DataExporter(
            file_format='invalid',
        )

        data_source = [
            {
                'id': 1,
                'name': 'Test',
            },
            {
                'id': 2,
                'name': 'Test2',
            }
        ]

        try:
            data_exporter.export_data(data_source)
        except ValueError as e:
            assert str(e) == 'Invalid export file format has been set.'
