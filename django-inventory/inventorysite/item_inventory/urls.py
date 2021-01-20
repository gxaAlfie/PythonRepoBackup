from django.conf.urls import url

from . import views

app_name = 'item_inventory'

urlpatterns = [
    url(r'^containers/(?P<pk>\d+)$', views.ContainerDetail.as_view(), name='show'),
    url(r'^containers/new$', views.ContainerCreate.as_view(), name='new'),
    url(r'^containers/edit/(?P<pk>\d+)$', views.ContainerUpdate.as_view(), name='update'),
    url(r'^containers/delete/(?P<pk>\d+)$', views.ContainerDelete.as_view(), name='delete'),

    url(r'^items/$', views.ItemList.as_view(), name='items_index'),
    url(r'^items/(?P<pk>\d+)$', views.ItemDetail.as_view(), name='items_show'),
    url(r'^items/new$', views.ItemCreate.as_view(), name='items_new'),
    url(r'^items/edit/(?P<pk>\d+)$', views.ItemUpdate.as_view(), name='items_update'),
    url(r'^items/delete/(?P<pk>\d+)$', views.ItemDelete.as_view(), name='items_delete'),

    url(r'^$', views.ContainerList.as_view(), name='index'),
]
