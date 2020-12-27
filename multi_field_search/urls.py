from django.urls import path
from multi_field_search.views import search

urlpatterns = [
    path('search', search, name='search')
]
