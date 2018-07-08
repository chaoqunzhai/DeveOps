from django.shortcuts import HttpResponse,redirect,render
from django.contrib.auth import authenticate,login,logout
from utils.session_auth import site_login

@site_login
def index(request):

    return render(request, "base/index.html", locals())

def Sinlogin(request):
    code = {}
    sessionid = request.session.session_key
    if sessionid:
        if request.session.get('login', None):
            return redirect('/login')
    if request.method == "POST":
        code = {"success": None}
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            request.session['login'] = True
            code["success"] = True
            return redirect(request.GET.get("next") or "/")
        else:
            # code = {"error": "用户名或者密码错误"}
            code["success"] = False

    return render(request, "base/login.html",locals())


def Sinlogout(request):
    if request.META.get("REMOTE_ADDR"):
        ipaddr = str(request.META.get("REMOTE_ADDR")).strip()
        # redis_conn.hdel("login",ipaddr)
    logout(request)

    return redirect("/")