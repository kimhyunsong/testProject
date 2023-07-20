from .models import Events
from django.http import HttpResponse
from .matches import get_data
from .serializers import EventsSerializer
from rest_framework.response import Response 
from rest_framework import status

# from .serializers import EventSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def get_matches(request):

    before_data = Events.objects.all()
    serializer = EventsSerializer(before_data, many=True)
    return HttpResponse(serializer.data, status=status.HTTP_201_CREATED)
    # get_data()

    # serializer = Event(data=request.data)
    # if serializer.is_valid(raise_exception=True):
    #     serializer.save(movie=movie, user=request.user)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)