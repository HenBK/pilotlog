from data_api.models import (Aircraft, Flight)  # noqa: F401


class DataImporter:
    """
    DataImporter class is responsible for importing data from a data source
    and persisting it into the system's database
    """
    def __init__(self, data_source, data_mapper):
        self.data_source = data_source
        self.data_mapper = data_mapper

    def import_data(self):
        """Import data from data source persisting it in the database"""

        mapped_data = self.data_mapper.map_data(self.data_source)

        # persist data in the database
        for row in mapped_data:
            model = self._get_model(row["model_name"])

            if model:
                # remove model name from the row as it is not a field in the db
                del row["model_name"]

                # create model instance and save it
                obj = model.objects.create(**row)
                obj.save()

        return mapped_data

    def _get_model(self, model_name):
        """Get model by name"""

        models = {
            "aircraft": "Aircraft",
            "flight": "Flight",
        }

        if model_name in models:
            return eval(models[model_name])
