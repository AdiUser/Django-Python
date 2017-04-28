from django.conf.urls import url
from . import views

app_name = "form"
urlpatterns = [
    url(r'show', views.show_response, name='ShowResponse'),
    url(r"^(?P<id>[0-9]+)/$", views.showIndex, name='showIndex'),
    url(r"form$", views.index, name='index')
]