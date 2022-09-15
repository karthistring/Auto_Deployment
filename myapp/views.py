
from myapp.models import TblEmp
from myapp.serialization import SerializationEmp
from rest_framework import permissions, status, generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import viewsets

# Create your views here.

class EmpViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication,
                              BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = SerializationEmp
    queryset = TblEmp.objects.all()

class EmpFilterview(generics.ListAPIView):
    authentication_classes = [SessionAuthentication,
                              BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = TblEmp.objects.all()
    serializer_class = SerializationEmp
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = {'name': ['exact'], 'age': ['exact']}
