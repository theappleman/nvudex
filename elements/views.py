from django.views.generic import ListView

from .models import Element

class ElementList(ListView):
    model = Element

element_list = ElementList.as_view()
