from django.urls import path
from . import views

urlpatterns = [
    # ... other URL patterns ...
    path('enregistrer_polygone/', views.enregistrer_polygone, name='enregistrer_polygone'),
    path('polygone/<int:polygone_id>/', views.afficher_surface, name='afficher_surface'),
]

