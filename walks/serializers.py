from django.db.models import fields
from walkers.models import Walker
from rest_framework import serializers
from .models import Walk

class WalkReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Walk
        fields = '__all__'
        depth = 2

class WalkCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Walk
        fields = '__all__'

    def validate(self, data):

        if data['beginning'] >= data['end']:
            raise serializers.ValidationError({'error': 'La fecha de inicio no puede ser mayor o igual a la fecha de fin'})
        elif not data['beginning'] or not data['end']:
            raise serializers.ValidationError({'error': 'Las fechas son requeridas'})
        
        return data

class WalkUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Walk
        fields = '__all__'
