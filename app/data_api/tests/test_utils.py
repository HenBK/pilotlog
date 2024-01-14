from datetime import time

from data_api.utils import (
    get_nested_value,
    seconds_to_time,
)


class TestUtils:
    """
    Test utils module
    """

    def test_get_nested_value(self):
        multiple_key_string = 'key1.key2.key3'
        multiple_nesting_dict = {
            'key1': {
                'key2': {
                    'key3': 'test_value_1',
                },
            },
        }

        no_nesting_key_string = 'key1'
        no_nesting_dict = {
            'key1': 'test_value_2',
        }

        assert get_nested_value(multiple_key_string, multiple_nesting_dict) == 'test_value_1'  # noqa
        assert get_nested_value(no_nesting_key_string, no_nesting_dict) == 'test_value_2'  # noqa

    def test_seconds_to_time(self):
        assert seconds_to_time(0) == time(hour=0, minute=0, second=0) 
        assert seconds_to_time(60) == time(hour=0, minute=1, second=0)
        assert seconds_to_time(3600) == time(hour=1, minute=0, second=0)
        assert seconds_to_time(3661) == time(hour=1, minute=1, second=1)
        assert seconds_to_time(86399) == time(hour=23, minute=59, second=59)
