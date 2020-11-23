from rest_framework import serializers
from lavado.models import Producto

class InsumosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ["nombre","precio","descripcion","stock"]
        