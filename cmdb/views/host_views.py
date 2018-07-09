from django.shortcuts import render
from django.http import JsonResponse
from utils.session_auth import site_login
from django.views.generic import View
# Create your views here.

@site_login
def hostlit(request):



    return render(request, "cmdb/index.html", locals())


class AssetExport(View):
    def post(self, request, *args, **kwargs):
        data = {}
        return JsonResponse(data)

    def get(self, request, *args, **kwargs):
        data = {}
        return JsonResponse(data)

class AssetCreate(View):
    def post(self, request, *args, **kwargs):
        data = {}
        return JsonResponse(data)

    def get(self, request, *args, **kwargs):
        data = {}
        return JsonResponse(data)

class AssetDowload(View):
    def post(self, request, *args, **kwargs):
        data = {}
        return JsonResponse(data)

    def get(self, request, *args, **kwargs):
        data = {}
        return JsonResponse(data)


class AssetNodeadd(View):
    def post(self, request, *args, **kwargs):
        data = {}

        return JsonResponse(data)

    def get(self, request, *args, **kwargs):

        return render(request,"cmdb/_asset_list_modal.html",locals())