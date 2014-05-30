from django.http import HttpResponse
from airquality.models import AirQuality
from datetime import datetime
import json, pytz

def hourly_data(request):
  latest_time = request.GET.get('time', 0)
  json_data = {}
  if latest_time == 0:
    latest_time = AirQuality.objects.order_by('-reptime')[0].reptime.__str__()
  for station in AirQuality.objects.values().filter(reptime = latest_time):
    json_data[station['stationcode']] = station
    hkt = pytz.timezone('Asia/Hong_Kong')
    json_data[station['stationcode']]['reptime'] = station['reptime'].astimezone(hkt).__str__()
  return HttpResponse(json.dumps(json_data), content_type="application/json")
