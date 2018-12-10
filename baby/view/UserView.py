from django.http import HttpResponse, JsonResponse
from ..models import BabyInfo,User
import json
from urllib import request

'''登录微信服务端'''


def wxLogin(req):
    APPID = "wxec3a4be3af18bb59"
    SECRET = "0be6ccb0bf3444085645fc6472bd2980"
    if req.method == "POST":
        body = req.body
        params = json.loads(body)
        code = params['code']
        avatarUrl=params['avatarUrl']
        nickName=params['nickName']
        print(params)
        # 调用微信code2session接口，获取openid
        WXURL = "https://api.weixin.qq.com/sns/jscode2session?appid={}&secret={}&js_code={}&grant_type=authorization_code".format(APPID, SECRET, code)
        print(WXURL)
        wxreq = request.Request(WXURL)
        wxres = request.urlopen(wxreq)
        wxres = wxres.read()
        # print(wxres.decode(encoding='utf-8'))
        r=json.loads(wxres,encoding='utf-8')
        print(r)
        errcode=r.get("errcode");
        print(errcode)
        # 组装返回结果对象
        result = {'openid': '123123123', 'session_key': 'qweqweqweqwe', 'unionid': 'dddddddddddddd', 'errcode': 0, 'errmsg': ''}
        return JsonResponse(result, safe=False, json_dumps_params={'ensure_ascii': False})

def userLogin(request):
    if request.method == "POST":
        body = request.body
        params = json.loads(body)
        username=params['username']
        userpwd=params['userpwd']
        # user=User.objects.get(Q(username=username),Q(userpwd=userpwd))
        user=User.objects.get(username=username,userpwd=userpwd)
        bid=user.bid_id
        print('bid:%s'%bid)
        baby=BabyInfo.objects.get(bid=str(bid))
        result={}
        b={}
        u={}
        u['uid']=user.uid
        u['nickname']=user.nickname
        u['avatarurl']=user.avatarurl
        b['bid']=baby.bid
        b['babyname']=baby.name
        if baby.sex=="A":
            b['babysex']="男"
        elif baby.sex=="B":
            b['babysex']="女"
        b['babyage']=baby.age
        b['babybirthday']=str(baby.birthday)
        b['babyheight']=baby.height
        b['babyweight']=baby.weight
        result['user']=u
        result['baby']=b
        print(result)
        return HttpResponse(json.dumps(result))
