import pytest

from django.urls import reverse


@pytest.mark.django_db
class TestDataApi:
    """
    Test data API "/import" endpoint
    """

    IMPORT_URL = reverse('data_api:import_data')

    def test_import_data(self, client):
        """
        Test that a valid file is imported successfully
        """

        with open('data_api/tests/test_data/test_import_file.json', 'rb') as test_file:  # noqa
            payload = {
                'file': test_file,
                'file_import_format': 'json',
                'file_export_format': 'csv',
            }
            res = client.post(self.IMPORT_URL, payload)

        assert res.status_code == 200
        assert res['Content-Disposition'] == 'attachment; filename="export_file.csv"'  # noqa
        assert res['Content-Type'] == 'text/csv'

    def test_invalid_import_file(self, client):
        """
        Test that an invalid file is not imported return a 400 response
        """

        with open('data_api/tests/test_data/test_invalid_import_file.txt', 'rb') as invalid_file:  # noqa
            payload = {
                'file': invalid_file,
                'file_import_format': 'json',
                'file_export_format': 'csv',
            }

            res = client.post(self.IMPORT_URL, payload)

        assert res.status_code == 400

    def test_import_format_not_specified(self, client):
        """
        Test that a request without an import format returns a 400 response
        """

        with open('data_api/tests/test_data/test_import_file.json', 'rb') as test_file:  # noqa
            payload = {
                'file': test_file,
                'file_export_format': 'csv',
            }

            res = client.post(self.IMPORT_URL, payload)

        assert res.status_code == 400

    def test_export_format_not_specified(self, client):
        """
        Test that a request without an export format returns a 400 response
        """

        with open('data_api/tests/test_data/test_import_file.json', 'rb') as test_file:  # noqa
            payload = {
                'file': test_file,
                'file_import_format': 'json',
            }

            res = client.post(self.IMPORT_URL, payload)

        assert res.status_code == 400
