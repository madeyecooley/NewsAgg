from django.conf.urls import url
from . import views

urlpatterns = [
    # /articles/
    url(r'^$', views.index, name='index'),
]
