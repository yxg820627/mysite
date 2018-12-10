from django.http import HttpResponse, JsonResponse
from..models import BabyRecord
import json

'''根据宝宝id获取宝宝喂养记录列表'''


def record(request):
    if request.method == "POST":
        postbody = request.body
        params = json.loads(postbody)
        bid = params['bid']
        print('bid=%s' % bid)
        records = BabyRecord.objects.filter(bid=bid).values('id', 'type', 'volume', 'starttime', 'endtime', 'recordtime', 'bid', 'uid')
        # records.query.group_by=['recordtime']
        # print(records)
        result = []
        for record in records:
            r={}
            r['id']=record['id']
            r['type']=record['type']
            r['volume']=record['volume']
            r['starttime']=str(record['starttime'])[11:]
            r['endtime']=str(record['endtime'])[11:]
            r['recordtime']=str(record['recordtime'])
            r['bid']=record['bid']
            r['uid']=record['uid']
            result.append(r)
        print(result)
        return HttpResponse(json.dumps(result))