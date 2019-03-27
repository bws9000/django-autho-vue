from django.shortcuts import render

from rest_framework.decorators import api_view
from django.http import HttpResponse


def public(request):
    return HttpResponse("You don't need to be authenticated to see this")


@api_view(['GET'])
def private(request):
    return HttpResponse("You should not see this message if not authenticated!")

    
def jwt_get_username_from_payload_handler(payload):
    return 'auth0user'
