from rest_framework import serializers

from car.models import Car


class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    manufacturer = serializers.CharField(max_length=64)
    model = serializers.CharField(max_length=64)
    horse_powers = serializers.IntegerField()
    is_broken = serializers.BooleanField()
    problem_description = serializers.CharField(
        required=False,
        allow_null=True
    )

    def validate_horse_powers(self, value):
        if not 1 <= value <= 1914:
            raise serializers.ValidationError(
                "Horse powers should be in 1-1914 gap."
            )
        else:
            return value

    def create(self, validated_data):
        return Car.objects.create(**validated_data)
