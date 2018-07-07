from django.conf.urls import url

from cmdb.views import host_views


urlpatterns = [

    url(r'^hostlist$',host_views.hostlit ,name="hostlist"),
    url(r'^asset-create$',host_views.AssetExport.as_view(),name="assetcreate"),


    url(r'^asset-node-add$',host_views.AssetNodeadd.as_view(),name="asset-node-add"),

    url(r'^asset-bulk-update$', host_views.AssetDowload.as_view(), name="assetdownload"),
    url(r'^asset-export$',host_views.AssetCreate.as_view(),name="assetexport")


]