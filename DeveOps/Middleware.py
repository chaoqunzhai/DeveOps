from django.conf import settings
# from backends.redis_conn import redis_conn as redis_conn_base
from django.shortcuts import HttpResponse,redirect,HttpResponseRedirect
# from ExcelhostList.plugins.site_logging import Logger
# from ExcelhostList.models import UserProfile
import datetime
#
#
# #钩子middleware方法！
# #在setting中添加配置，相当于全局都需要过这个middeware插件
# #setting中的MIDDLEWARE 是从上到下顺序执行，如果上面中有一个MIDDLEWARE没有通过,那后面也都不会执行

# redis_conn = redis_conn_base(django_settings=settings,db=3)
import re

exclued_path = [re.compile(item) for item in settings.EXCLUDE_URL]

class SimpleMiddleware(object):


    def process_request(self, request):
        url_path = request.path
        for each in exclued_path:
            if re.match(each, url_path):
                return
        # if hasattr(request,'session'):
        #     is_login = request.session.get('login',None)
        #     #request.session.set_expiry(0)
        # else:
        #     session_obj=getattr(request.request, 'session')
        #     is_login = session_obj._get_session().get('login',None)
        #     #request.request.session.set_expiry(0)
        # # print('site_login',is_login)
        # if is_login:
        #     pass
        # else:
        #     return HttpResponseRedirect("/login")

    #     #进入视图之前会先进入这里
    #     #捕用户访问view的时候，就会先经过这里，然后才去调用view视图函数，所以这里可以拿到很多信息
    def process_view(self,request,view_func,view_args,view_kwargs):
        date_now = (datetime.datetime.now()).strftime('%Y-%m-%d %H:%M:%S')
        #在视图调用之前调用的这个 process_view
        ##所以可以拿到很多对端的各种信息，例如IP，请求头的所以东西等等
        # setattr(request,) view_args,view_kwargs

        #print("process_view____视图调用之前会先执行这个process_view:",request.path,view_func)

        print("-process_view____视图调用之前会先执行这个process_view",request)
    def process_exception(self, request, exception):

        # Logger().log(
        #     str('用户:[%s],模块:后台错误日志记录,错误信息:%s' % (request.user, exception)),
        #     True)
        # return HttpResponse("<h1>您访问的页面%s不存在！错误信息:%s,%s</h1>" % (exception, request, exception))
        pass
    def process_response(self, request, response):
        return response
#
