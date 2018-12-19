
from django.conf.urls import url

from . import views

app_name = "species"
urlpatterns = [
    url(r'(?P<slug>\w+)/?$', views.species_detail, name="species_detail"),
]
