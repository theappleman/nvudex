from django.conf.urls import url

from . import views

app_name = "elements"
urlpatterns = [
    url(r'(?P<slug>\w+)/?$', views.element_detail, name="element_detail"),
    url(r'^$', views.element_list, name="element_list"),
]
