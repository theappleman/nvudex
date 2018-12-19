from django.views.generic import DetailView, ListView

from .models import Element

class ElementList(ListView):
    model = Element

element_list = ElementList.as_view()

class ElementDetail(DetailView):
    model = Element
    slug_field = 'identifier'

    def get_context_data(self, *args, **kwargs):
        context = super(ElementDetail, self).get_context_data(*args, **kwargs)
        context['species_list'] = self.object.species_set.all()

        return context

element_detail = ElementDetail.as_view()
