from django.shortcuts import render, HttpResponse
from django.views.generic import View
from django.http import JsonResponse
from cmdb.models.node import Node
import json
import uuid

def nodelist(request):

    nodeall = Node.objects.all()
    callback = []
    for i in nodeall:
        value={"id":i.id,
             "key":i.key,
             "value":i.value,
             "parent":i.parent.id,
            "assets_amount": 0,
            "is_node": True
             }
        callback.append(value)
    data = {'statuc': 200, 'value': callback}

    return JsonResponse(data)


#/api/assets/v1/assets/?node_id
class Assetlist(View):
    #previous:上一页
    #next:下一页
    def get(self, request, *args, **kwargs):
        node_id = request.GET.get("node_id")
        show_current_asset = request.GET.get("show_current_asset","")
        order = request.GET.get("order","")
        search = request.GET.get("order","")
        limit = request.GET.get("limit","")
        offset = request.GET.get("offset", "")

        a = {"count": 0, "next": None, "previous": None, "results": []}

        if node_id == "3ce04dc6-f013-4b6f-b0fe-429b664e98f7":

            data = {
                "id": '1',
                "hostname": "ceshi",
                "ip": "192.168.5.100",
                "hardware": "00：",
                "is_active":True,
                "is_connective": True,
                "nodes":[
                    "473c8b1ad0484062b061d767032ff73a",
                    "0116f2bb7836488d8322a5aeb5384788"
                ]

            }

            a={"count":1,"next":None,"previous":None,"results":[data]}


        print("asset-list",node_id)


        return JsonResponse(a)


class AssetUpdate(View):

    def post(self, request, *args, **kwargs):
        data = {}
        return JsonResponse(data)

    def get(self, request, *args, **kwargs):
        data = {}
        return JsonResponse(data)




class NodeChildrenAdd(View):

    def post(self, request, *args, **kwargs):

        data = {"status":None,"data":None}

        nodeid_id = request.POST.get("nodeid")
        # print("NodeChildren->在次节点下创建目录",nodeid_id)
        if nodeid_id:
            this_obj = Node.objects.get(id=nodeid_id)
            this_obj.create_child("NodeNew")
            data = {"status": "success", "data": {"id": this_obj.id,
                                                  "value": "NodeNew",
                                                  "assets_amount":0}}

        return JsonResponse(data)

    def get(self, request, *args, **kwargs):
        data = {}
        return JsonResponse(data)

class AssetDetail(View):

    def post(self, request, *args, **kwargs):
        data = {}
        return JsonResponse(data)

    def get(self, request, *args, **kwargs):
        data = {}
        return JsonResponse(data)

class NodeDeatil(View):

    def post(self, request, *args, **kwargs):

        data = {}

        body = json.loads(str(request.body, encoding="utf-8"))

        print("NodeDeatil",request.POST.get("treeNodeId"),body)
        if body:

            this_obj = Node.objects.get(id=body.get("id"))
            this_obj.objects.update(value=body.get("value"))
            this_obj.save()
        return JsonResponse(data)

    def get(self, request, *args, **kwargs):
        data = {}
        return JsonResponse(data)

    def delete(self,request,*args,**kwargs):
        data = {"status":None}
        print("str(request.body",str(request.body,encoding="utf-8"))
        body = json.loads(str(request.body, encoding="utf-8"))


        if body:
            Node.objects.filter(id=body.get("id")).delete()
            data["status"] = "success"
        return JsonResponse(data)
class NodeRefresh(View):

    def post(self, request, *args, **kwargs):
        data = {}
        return JsonResponse(data)

    def get(self, request, *args, **kwargs):
        data = {}
        return JsonResponse(data)

class NodeRename(View):

    def post(self, request, *args, **kwargs):

        data = {}

        body = json.loads(str(request.body, encoding="utf-8"))


        if body:

            Node.objects.filter(id=body.get("id")).update(value=body.get("value"))
        return JsonResponse(data)

    def get(self, request, *args, **kwargs):
        data = {}
        return JsonResponse(data)


class AssetMove(View):

    def post(self, request, *args, **kwargs):
        data = {}
        return JsonResponse(data)

    def get(self, request, *args, **kwargs):
        data = {}
        return JsonResponse(data)

class ChildrenMove(View):
    #可以同时移动n多个ode
    def post(self, request, *args, **kwargs):
        data = {}

        body = json.loads(str(request.body, encoding="utf-8"))
        if body:
            parent_id = body.get("parent_id")
            parent_obj = Node.objects.get(id=parent_id)
            if parent_id and len(body.get("treeid")) >0:
                for tree_id in body.get("treeid"):
                    tree_obj = Node.objects.get(id=tree_id)
                    tree_obj.parent = parent_obj

        return JsonResponse(data)

    def get(self, request, *args, **kwargs):
        data = {}
        return JsonResponse(data)

class NodeTest(View):

    def post(self, request, *args, **kwargs):
        data = {}
        return JsonResponse(data)

    def get(self, request, *args, **kwargs):
        data = {}
        return JsonResponse(data)
