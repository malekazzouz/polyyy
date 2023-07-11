from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog.views import enregistrer_polygone, afficher_surface

class TestUrls(SimpleTestCase):
    
    def test_enregistrer_polygone_url_resolves(self):
        url = reverse('enregistrer_polygone')
        self.assertEquals(resolve(url).func, enregistrer_polygone)

from django.test import TestCase
from django.urls import reverse
from blog.models import Polygone

class EnregistrerPolygoneViewTest(TestCase):

    def test_enregistrer_polygone(self):
        # Créer les données de test
        nom = "Polygone test"
        coordonnees = "POLYGON((0 0, 0 5, 5 5, 5 0, 0 0))"
        # Envoyer une requête POST à la vue avec les données de test
        response = self.client.post(reverse('enregistrer_polygone'), {'nom': nom, 'coordonnees': coordonnees})

        # Vérifier que la réponse a un statut HTTP 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Vérifier que le polygone a été enregistré en base de données
        polygone = Polygone.objects.get(nom=nom)
        self.assertEqual(polygone.coordonnees, coordonnees)

   
# Create your tests here.

