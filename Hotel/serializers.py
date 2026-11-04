from rest_framework import serializers
from .models import HotelDb, CustomerDb, BookingDb
from django.utils import timezone


class HotelSerializer(serializers.ModelSerializer):

    class Meta:
        model = HotelDb
        fields = "__all__"
        read_only_fields = ["id"]


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerDb
        fields = "__all__"
        read_only_fields = ["id"]


class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookingDb
        fields = "__all__"
        read_only_fields = ["id", "total_amount"]

    def validate(self, validated_data):

        check_in = validated_data.get("check_in")
        check_out = validated_data.get("check_out")
        hotel = validated_data.get("hotel")

        # Check-in date validation
        if check_in < timezone.localdate():
            raise serializers.ValidationError(
                "Check-in date cannot be in the past"
            )

        # Check-out date validation
        if check_out <= check_in:
            raise serializers.ValidationError(
                "Check-out date must be after check-in date"
            )

        # Overlapping booking validation
        if BookingDb.objects.filter(
            hotel=hotel,
            check_in__lt=check_out,
            check_out__gt=check_in
        ).exists():

            raise serializers.ValidationError(
                "Hotel is already booked for these dates"
            )

        return validated_data