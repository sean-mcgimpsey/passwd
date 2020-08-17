from django.shortcuts import render
from rest_framework import viewsets
from .serializers import secretSerializer
from .models import secret
from .tasks import sleepy
from rest_framework.generics import ( ListAPIView ) 
# Create your views here.


class secretViewSet(viewsets.ModelViewSet):
    queryset = secret.objects.all()
    serializer_class = secretSerializer

class retrieveSecretView(ListAPIView):
    serializer_class = secretSerializer

    def get_queryset(self):
        access_code = self.request.query_params.get('access_code', None)
        qs = secret.objects.all()
        if access_code is None:
            return Response({"message": "Invalid data received"}, status=HTTP_400_BAD_REQUEST)
        return qs.filter(access_code=access_code)

