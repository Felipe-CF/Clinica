from rest_framework import serializers
from backend.models.profisssional import Profissional, Usuario

class ProfissionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profissional
        fields = '__all__'
        
    def create(self, validated_data):
        profisssional = Profissional.objects.create(**validated_data)
        return profisssional
