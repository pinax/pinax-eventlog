from rest_framework.generics import CreateAPIView
from rest_framework.renderers import JSONRenderer

from .models import Log
from .serializers import LogSerializer


class LogEventCreate(CreateAPIView):
    model = Log
    serializer_class = LogSerializer
    renderer_classes = (JSONRenderer, )
