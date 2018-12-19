from django.urls import url

from . import views

app_name = "elements"
urlpatterns = [
    url('r^$', views.element_list, name="element_list"),
]
