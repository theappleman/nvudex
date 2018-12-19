from django.views.generic import DetailView

from .models import *

class SpeciesDetail(DetailView):
    model = Species
    slug_field = 'identifier'

species_detail = SpeciesDetail.as_view()
