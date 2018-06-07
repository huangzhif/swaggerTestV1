# coding:utf-8
import json
import traceback
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


# Create your views here.


def api_account_login(request):
    """用户登录"""
    account = request.POST.get('account', None)
    password = request.POST.get('password', None)

    user = User.objects.filter(username=account).first()

    if not user:
        return HttpResponse(json.dumps(u'用户不存在',
                                       ensure_ascii=False), content_type="application/json")

    account = user.username
    try:
        user = authenticate(username=account, password=password)
        if user:
            login(request, user)
            result = {"c": '1', "data": {'uid': user.pk}}

        else:
            result = u'用户或密码验证错误'

        return HttpResponse(json.dumps(result, ensure_ascii=False), content_type="application/json")
    except (BaseException,):

        s_err_info = traceback.format_exc()
        dict_resp = {"c": -1, "m": s_err_info}
        return HttpResponse(json.dumps(dict_resp, ensure_ascii=False), content_type="application/json")
