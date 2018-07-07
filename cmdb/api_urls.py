from django.conf.urls import url

from cmdb.views import api_views

urlpatterns = [
    #Tree 选择请求数据
    url(r'^asset-list$',api_views.Assetlist.as_view(),name="assetlist"),

    url(r'^asset-update$',api_views.AssetUpdate.as_view(),name="assetupdate"),
    url(r'^asset-detail$', api_views.AssetDetail.as_view(), name="assetdetail"),


    url(r'^assetmove',api_views.AssetMove.as_view(),name="assetmove"),

    url(r'^node-list', api_views.nodelist, name="nodelist"),

    #editTreeNode and removeTreeNode
    url(r'^node-detail', api_views.NodeDeatil.as_view(), name="nodedetail"),

    #addTreeNode
    url(r'^node-children$', api_views.NodeChildrenAdd.as_view(), name="nodechildren"),


    #renameNode
    url(r'^node-rname-children', api_views.NodeRename.as_view(), name="noderename"),


    url(r'^node-move-children', api_views.ChildrenMove.as_view(), name="nodeMove"),

    url(r'^node-refresh-hardware-info', api_views.NodeRefresh.as_view(), name="noderefresh"),
    url(r'^node-test', api_views.NodeTest.as_view(), name="nodetest"),







]