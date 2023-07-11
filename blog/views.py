from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.gis.geos import GEOSGeometry
from shapely.geometry import shape
from .models import Polygone

from django.shortcuts import render
from django.http import JsonResponse

def enregistrer_polygone(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        coordonnees = request.POST.get('coordonnees')

        # Convertir les coordonnées en format valide
        polygone_geom = GEOSGeometry(coordonnees)
        polygone = Polygone(nom=nom, coordonnees=polygone_geom)
        polygone.save()
        
        

        # Réponse JSON indiquant que le polygone a été enregistré avec succès
        data = {'message': 'Polygone enregistré avec succès !'}
        return JsonResponse(data)

    return render(request, 'blog/enregistrer_polygone.html')
from django.shortcuts import render
from .models import Polygone

def afficher_surface(request, polygone_id):
    polygone = Polygone.objects.get(id=polygone_id)
    surface = polygone.coordonnees.area  # Calcule la surface du polygone en utilisant la méthode `area` du champ PolygonField

    context = {
        'polygone': polygone,
        'surface': surface,
    }
    return render(request, 'blog/surface.html', context)

