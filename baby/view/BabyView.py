from ..models import BabyInfo
from django.http import HttpResponse, JsonResponse

'''获取宝宝列表'''


def index(request):
    babys = BabyInfo.objects.values('bid', 'name', 'sex', 'age', 'birthday')
    result = list(babys)
    return JsonResponse(result, safe=False, json_dumps_params={'ensure_ascii': False})


'''根据宝宝id获取宝宝信息'''


def getBabyById(request):
    if request.method == "POST":
        bid = request.POST.get("bid")
        babys = BabyInfo.objects.filter(bid=bid).values('bid', 'name', 'sex', 'age', 'birthday')
        result = list(babys)
        return JsonResponse(result, safe=False, json_dumps_params={'ensure_ascii': False})