from django.urls import path
from .views import show_all_records


urlpatterns = [
    path('all/', show_all_records, name='show_all_records'),
    
]
