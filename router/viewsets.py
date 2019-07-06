import json

from django.http import HttpResponse

from rest_framework import viewsets
from rest_framework.exceptions import ParseError
from rest_framework.parsers import JSONParser

from .serializers import RouterSerializer
from .router import router


class RouterViewset(viewsets.ViewSet):
    parsers = (JSONParser, )

    def create(self, request):
        if not request.data:
            raise ParseError('No json file uploaded')
        input_json = json.loads(request.data.keys()[0])
        try:
            result = router(input_json)
        except Exception as e:
            return HttpResponse('Error in routing: %s' % e.message)
        return HttpResponse(json.dumps(result), 'application/json')
