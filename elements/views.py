from django.views.generic import DetailView, ListView

from .models import Element

class ElementList(ListView):
    model = Element

element_list = ElementList.as_view()

class ElementDetail(DetailView):
    model = Element
    slug_field = 'identifier'

element_detail = ElementDetail.as_view()
