from rest_framework import serializers
from backend.models.paciente import Paciente

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'
        
    def create(self, validated_data):
        paciente = Paciente.objects.create(**validated_data)
        return paciente
