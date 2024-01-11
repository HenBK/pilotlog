"""
URL mappings for the data API
"""

from django.urls import path

from data_api import views

app_name = 'data_api'

urlpatterns = [
    path('import/', views.ImportDataView.as_view(), name='import_data'),
]
