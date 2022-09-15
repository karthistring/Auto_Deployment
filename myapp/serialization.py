from myapp.models import TblEmp
from rest_framework import serializers

class SerializationEmp(serializers.ModelSerializer):
    class Meta:
        model = TblEmp
        fields = '__all__'