from .models import Events
from django.http import HttpResponse
from .matches import get_data
from .serializers import EventsSerializer
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.decorators import api_view
interval_seconds = 300

def index(request):
    return HttpResponse(status.HTTP_200_OK)


@api_view(['GET','POST'])
def change_interval(request):
    if request.method == 'GET':
        events = Events.objects.all()
        serializer = EventsSerializer(events, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        interval_seconds = int(request.data['data'])
        return Response(status.HTTP_202_ACCEPTED)

