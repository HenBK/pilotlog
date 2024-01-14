import pytest

from data_api.data_handler import DataHandler


@pytest.mark.django_db
class TestDataHandler:
    """
    Test data handler class
    """

    def test_process_data(self, mocker):
        """
        Test that data is processed correctly by the data handler
        checking each "process_data" function step is called correctly
        """

        data_handler = DataHandler(
            import_format='json',
            export_format='csv',
        )

        test_data = [
            {
                '_modified': 1616317613,
                'guid': '00000000-0000-0000-0000-000000000367',
                'meta': {
                    'Active': True,
                    'Aerobatic': False,
                    'AircraftCode': '00000000-0000-0000-0000-000000000367',
                    'Category': 1,
                    'Class': 5,
                    'Company': 'Other',
                    'Complex': False,
                    'CondLog': 69,
                    'DefaultApp': 0,
                    'DefaultLaunch': 0,
                    'DefaultLog': 2,
                    'DefaultOps': 0,
                    'DeviceCode': 1,
                    'Efis': False,
                    'FNPT': 0,
                    'FavList': False,
                    'Fin': '',
                    'HighPerf': False,
                    'Kg5700': False,
                    'Make': 'Cessna',
                    'Model': 'C150',
                    'Power': 1,
                    'Rating': '',
                    'Record_Modified': 1616320991,
                    'RefSearch': 'PHALI',
                    'Reference': 'PH-ALI',
                    'Run2': False,
                    'Sea': False,
                    'Seats': 0,
                    'SubModel': '',
                    'TMG': False,
                    'Tailwheel': False
                },
                'platform': 9,
                'table': 'Aircraft',
                'user_id': 125880
            },
            {
                '_modified': 1616317613,
                'guid': '00000000-0000-0000-0000-000000009940',
                'meta': {'AircraftCode': '00000000-0000-0000-0000-000000000427',  # noqa
                         'ArrCode': '00000000-0000-0000-0000-000000009512',
                         'ArrOffset': 60,
                         'ArrRwy': '',
                         'ArrTimeSCHED': 0,
                         'ArrTimeUTC': 735,
                         'BaseOffset': 120,
                         'CrewList': '',
                         'DateBASE': '2008-08-14',
                         'DateLOCAL': '2008-08-14',
                         'DateUTC': '2008-08-14',
                         'DeIce': False,
                         'DepCode': '00000000-0000-0000-0000-000000009971',
                         'DepOffset': 120,
                         'DepRwy': '',
                         'DepTimeSCHED': 0,
                         'DepTimeUTC': 617,
                         'FlightCode': '00000000-0000-0000-0000-000000009940',
                         'FlightNumber': '551',
                         'FlightSearch': '20080814:551WROLTN',
                         'Fuel': 0,
                         'FuelPlanned': 0,
                         'FuelUsed': 0,
                         'HobbsIn': 0,
                         'HobbsOut': 0,
                         'Holding': 0,
                         'LdgDay': 1,
                         'LdgNight': 0,
                         'LdgTimeUTC': 0,
                         'LiftSW': 0,
                         'NextPage': False,
                         'NextSummary': False,
                         'P1Code': '00000000-0000-0000-0000-000000000780',
                         'P2Code': '00000000-0000-0000-0000-000000000001',
                         'P3Code': '00000000-0000-0000-0000-000000000000',
                         'P4Code': '00000000-0000-0000-0000-000000000000',
                         'PF': True,
                         'Pairing': '',
                         'Pax': 0,
                         'Record_Modified': 1616320991,
                         'Remarks': 'ILS26 manual, a/thrust off',
                         'Report': '',
                         'Route': '',
                         'SignBox': 0,
                         'TagApproach': '401',
                         'TagDelay': '',
                         'TagLaunch': '',
                         'TagLesson': '',
                         'TagOps': '',
                         'ToDay': 1,
                         'ToEdit': False,
                         'ToNight': 0,
                         'ToTimeUTC': 0,
                         'Training': '',
                         'UserBool': False,
                         'UserNum': 0,
                         'UserText': '',
                         'minAIR': 0,
                         'minCOP': 118,
                         'minDUAL': 0,
                         'minEXAM': 0,
                         'minIFR': 118,
                         'minIMT': 0,
                         'minINSTR': 0,
                         'minNIGHT': 0,
                         'minPIC': 0,
                         'minPICUS': 0,
                         'minREL': 0,
                         'minSFR': 0,
                         'minTOTAL': 118,
                         'minU1': 0,
                         'minU2': 0,
                         'minU3': 0,
                         'minU4': 0,
                         'minXC': 118},
                'platform': 9,
                'table': 'Flight',
                'user_id': 125880
            },
        ]

        mocked_parse_data_source = mocker.patch.object(
            data_handler,
            '_parse_data_source',
            return_value=test_data,
        )
        mocked_import_data = mocker.patch.object(
            data_handler,
            '_import_data',
            return_value=test_data,
        )
        mocked_export_data = mocker.patch.object(
            data_handler,
            '_export_data',
            return_value=test_data,
        )

        processed_data = data_handler.process_data(test_data)

        mocked_parse_data_source.assert_called_once_with(
            file_format=data_handler.import_format,
            data_source=test_data,
        )
        mocked_import_data.assert_called_once_with(test_data)
        mocked_export_data.assert_called_once_with(test_data)
        assert processed_data == test_data

    def test_process_data_invalid_export_format(self, mocker):
        """
        Test that data handler raises ValueError when invalid export format
        """

        data_handler = DataHandler(
            import_format='json',
            export_format='invalid',
        )

        mocker.patch.object(
            data_handler,
            '_parse_data_source',
            return_value=[],
        )

        with pytest.raises(ValueError) as e:
            data_handler.process_data([])
            assert str(e) == "Invalid export file format has been set."

    def test_process_data_invalid_import_format(self, mocker):
        """
        Test that data handler raises ValueError when invalid import format
        """

        data_handler = DataHandler(
            import_format='invalid',
            export_format='csv',
        )

        mocker.patch.object(
            data_handler,
            '_parse_data_source',
            return_value=[],
        )

        with pytest.raises(ValueError) as e:
            data_handler.process_data([])
            assert str(e) == "Invalid export file format has been set."
