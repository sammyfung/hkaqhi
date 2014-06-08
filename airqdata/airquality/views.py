from django.http import HttpResponse
from airquality.models import AirQuality
from datetime import datetime, timedelta
import json, pytz

def hourly_data(request):
  latest_time = request.GET.get('time', 0)
  json_data = {}
  if latest_time == 0:
    latest_time = AirQuality.objects.order_by('-reptime')[0].reptime.__str__()
  for station in AirQuality.objects.values().filter(reptime = latest_time):
    json_data[station['stationcode']] = station
<<<<<<< HEAD
    json_data[station['stationcode']]['reptime'] = station['reptime'] + datetime.timedelta(hours=8)
=======
    hkt = pytz.timezone('Asia/Hong_Kong')
    json_data[station['stationcode']]['reptime'] = station['reptime'].astimezone(hkt).__str__()
  return HttpResponse(json.dumps(json_data), content_type="application/json")

def station_data(request):
  request_id = request.GET.get('id',0)
  current_time = datetime.now() - timedelta(days=1)
  json_data = {}
  i = 0
  for hourly in AirQuality.objects.values().filter(stationid = request_id, reptime__gte = current_time):
    json_data[i] = hourly
    hkt = pytz.timezone('Asia/Hong_Kong')
    json_data[i]['reptime'] = hourly['reptime'].astimezone(hkt).__str__()
    i += 1
>>>>>>> 8fd5b619726cd673435d104c067fa1c60ef1512a
  return HttpResponse(json.dumps(json_data), content_type="application/json")
