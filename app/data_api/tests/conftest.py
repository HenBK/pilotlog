import pytest

from mixer.backend.django import mixer

from data_api.models import MapperConfig


@pytest.fixture
def mapper_configs():
    test_model_configs = {
        'flight': {
            'target_fields': [
                'Date',
                'AircraftID',
                'From',
                'To',
                'Route',
                'TimeOut',
                'TimeOff',
                'TimeOn',
                'TimeIn',
                'OnDuty',
                'OffDuty',
                'TotalTime',
                'PIC',
                'SIC',
                'Night',
                'Solo',
                'CrossCountry',
                'NVG',
                'NVGOps',
                'Distance',
                'DayTakeoffs',
                'DayLandingsFullStop',
                'NightLandingsFullStop',
                'AllLandings',
                'ActualInstrument',
                'SimulatedInstrument',
                'HobbsStart',
                'HobbsEnd',
                'TachStart',
                'TachEnd',
                'Holds',
                'Approach1',
                'Approach2',
                'Approach3',
                'Approach4',
                'Approach5',
                'Approach6',
                'DualGiven',
                'DualReceived',
                'SimulatedFlight',
                'GroundTraining',
                'InstructorName',
                'InstructorComments',
                'Person1',
                'Person2',
                'Person3',
                'Person4',
                'Person5',
                'Person6',
                'FlightReview',
                'Checkride',
                'IPC',
                'NVGProficiency',
                'FAA6158',
                'CustomFieldNameText',
                'CustomFieldNameNumeric',
                'CustomFieldNameHours',
                'CustomFieldNameCounter',
                'CustomFieldNameDate',
                'CustomFieldNameDateTime',
                'CustomFieldNameToggle',
                'PilotComments',
            ],
            'fields_mapping': {
                'meta.DateUTC': {
                    'type': 'date',
                    'target': 'Date',
                },
                'meta.AircraftCode': {
                    'type': 'string',
                    'target': 'AircraftID',
                },
                'meta.DepCode': {
                    'type': 'string',
                    'target': 'From',
                },
                'meta.ArrCode': {
                    'type': 'string',
                    'target': 'To',
                },
                'meta.Route': {
                    'type': 'string',
                    'target': 'Route',
                },
                'meta.DepTimeUTC': {
                    'type': 'time',
                    'target': 'TimeOut',
                },
                'meta.ArrTimeUTC': {
                    'type': 'time',
                    'target': 'TimeIn',
                },
                'meta.minTotal': {
                    'type': 'decimal',
                    'target': 'TotalTime',
                },
                'meta.minPIC': {
                    'type': 'decimal',
                    'target': 'PIC',
                },
                'meta.minSIC': {
                    'type': 'decimal',
                    'target': 'SIC',
                },
                'meta.minNight': {
                    'type': 'decimal',
                    'target': 'Night',
                },
                'meta.minXC': {
                    'type': 'decimal',
                    'target': 'CrossCountry',
                },
                'meta.LdgDay': {
                    'type': 'integer',
                    'target': 'DayTakeoffs',
                },
                'meta.LdgNight': {
                    'type': 'integer',
                    'target': 'NightTakeoffs',
                },
                'meta.HobbsIn': {
                    'type': 'decimal',
                    'target': 'HobbsStart',
                },
                'meta.HobbsOut': {
                    'type': 'decimal',
                    'target': 'HobbsEnd',
                },
                'meta.Holding': {
                    'type': 'integer',
                    'target': 'Holds',
                },
                'meta.minDUAL': {
                    'type': 'decimal',
                    'target': 'DualGiven',
                },
                'meta.Remarks': {
                    'type': 'string',
                    'target': 'InstructorComments',
                },
            }
        },
        'aircraft': {
            'target_fields': [
                'AircraftID',
                'EquipmentType',
                'TypeCode',
                'Year',
                'Make',
                'Model',
                'Category',
                'Class',
                'GearType',
                'EngineType',
                'Complex',
                'HighPerformance',
                'Pressurized',
                'TAA',
            ],
            'fields_mapping': {
                'meta.AircraftCode': {
                    'type': 'string',
                    'target': 'AircraftID',
                },
                'meta.DeviceCode': {
                    'type': 'string',
                    'target': 'TypeCode',
                },
                'meta.Make': {
                    'type': 'string',
                    'target': 'Make',
                },
                'meta.Model': {
                    'type': 'string',
                    'target': 'Model',
                },
                'meta.Category': {
                    'type': 'string',
                    'target': 'Category',
                },
                'meta.Class': {
                    'type': 'string',
                    'target': 'Class',
                },
                'meta.Complex': {
                    'type': 'boolean',
                    'target': 'Complex',
                },
                'meta.HighPerf': {
                    'type': 'boolean',
                    'target': 'HighPerformance',
                },
            }
        }
    }

    configs = []

    for model_name, config in test_model_configs.items():
        configs.append(mixer.blend(
            MapperConfig,
            model_name=model_name,
            config=config,
        ))

    return configs
