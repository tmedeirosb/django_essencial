from django.conf.urls import url
from . import views

urlpatterns = [
                url(r'^$', views.page, name='index'),
                url(r'^(?P<slug>[\w./-]+)/$', views.page, name='page')
              ]

