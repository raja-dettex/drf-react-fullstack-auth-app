from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def endpoint_list(request):
    data = [
        'api/token',
        'api/token/refresh'
    ]
    return Response(data)