from data_api.models import MapperConfig
from data_api.utils import (
    get_nested_value,
    seconds_to_time,
)


class DataMapper:
    """
    DataMapper class is responsible for mapping data from a data source
    to the exported configuration format
    """
    def __init__(self, mapping_config=None):
        self.mapping_config = mapping_config or self._get_mapping_config()

    def _get_mapping_config(self):
        """
        Get mapping configuration from the database,
        the structure of the mapping configuration is as follows:
        {
            "model_name": {
                "target_fields": ["field_name", ...], # list of field names in final mapped data
                "fields_mapping": { # mapping of source field names to target field names
                    "source_field_name": { # field name as it comes in source file
                        "target": "target_field_name", # field name in database
                        "type": "field_type" # field type
                    },
                    ...
            }
        }
        """ # noqa
        mapping_config = {}

        configs = MapperConfig.objects.all()

        for config_record in configs:
            model_name = config_record.model_name.lower()
            mapping_config[model_name] = config_record.config

        return mapping_config

    def map_data(self, data_source):
        """Maps data from data source to the exported configuration format"""

        mapped_data = []

        for row in data_source:
            model_name = row.get("table", None)

            if not model_name:
                raise ValueError(
                    "Invalid data source, table name is missing for a record"
                )
            else:
                model_name = model_name.lower()

            # skip rows for models that do not have mappping configured
            if model_name not in self.mapping_config:
                continue

            model_config_fields = self.mapping_config[model_name]

            target_fields = model_config_fields['target_fields']

            # initialize dict to store mapped fields
            mapped_row = {field: None for field in target_fields}

            # map fields from the source to the target fields
            for field_name in model_config_fields['fields_mapping'].keys():
                value = get_nested_value(field_name, row)

                # cast 'time' type fields into python datetime.time object
                if (
                    value is not None
                    and model_config_fields['fields_mapping'][field_name]['type'] == 'time'  # noqa
                ):
                    value = seconds_to_time(value)

                target_field = (
                    model_config_fields['fields_mapping'][field_name]['target']
                )
                mapped_row[target_field] = value

            mapped_row["model_name"] = model_name
            mapped_data.append(mapped_row)

        mapped_data.sort(key=lambda x: x['model_name'])

        return mapped_data
