from django.contrib import admin
from django.urls import path

from .views import *
from . import views
urlpatterns = [
    path('', index, name="index"),
    path('charts', charts, name="charts"),
    path('crypto', crypto, name="crypto"),
    path('get_crypto_data/', get_crypto_data, name='get_crypto_data'),
    path('info/', info, name="info"),
    path('login/', login, name="login"),
    path('edit-all/', edit_all_ghadi, name='edit_all_ghadi'),
    path('create-default/', create_default_data, name='create_default_data'),
    path('get_table_data/', GetTableDataView.as_view(), name='get_table_data'),

]
