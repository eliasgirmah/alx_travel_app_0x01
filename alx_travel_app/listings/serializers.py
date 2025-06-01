from rest_framework import serializers
from .models import Listing, Booking

# Serializer for the Listing model
class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'  # Includes all fields from the model


# Serializer for the Booking model
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'  # Includes all fields from the model
