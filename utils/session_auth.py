from django.conf import settings
from django.shortcuts import redirect

#todo：自定义登陆
def site_login(func):
    def warpper(*args,**kwargs):
        request=args[0]
        if hasattr(request,'session'):
            is_login = request.session.get('login',None)
            #request.session.set_expiry(0)
        else:
            session_obj=getattr(request.request, 'session')
            is_login = session_obj._get_session().get('login',None)
            #request.request.session.set_expiry(0)
        # print('site_login',is_login)
        if is_login:
            respon = func(*args,**kwargs)

            return respon
        else:
            return redirect('/login')
    return warpper
