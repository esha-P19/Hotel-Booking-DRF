from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from Hotel.models import HotelDb, CustomerDb, BookingDb
from Hotel.serializers import HotelSerializer, CustomerSerializer, BookingSerializer

from decimal import Decimal


#HOTEL 

class HotelListCreateView(APIView):

    def get(self, request):

        qs = HotelDb.objects.all()

        serializer_instance = HotelSerializer(qs, many=True)

        return Response(data=serializer_instance.data)

    def post(self, request):

        form_data = request.data

        serializer_instance = HotelSerializer(data=form_data)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)

        else:

            return Response(data=serializer_instance.errors)


class HotelRetrieveUpdateDeleteView(APIView):

    def get(self, request, pk):

        qs = get_object_or_404(HotelDb, id=pk)

        serializer_instance = HotelSerializer(qs)

        return Response(data=serializer_instance.data)

    def put(self, request, pk):

        form_data = request.data

        hotel_object = get_object_or_404(
            HotelDb,
            id=pk
        )

        serializer_instance = HotelSerializer(
            data=form_data,
            instance=hotel_object
        )

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)

        else:

            return Response(data=serializer_instance.errors)

    def delete(self, request, pk):

        hotel_object = get_object_or_404(
            HotelDb,
            id=pk
        )

        hotel_object.delete()

        return Response(
            data={"message": "Deleted...!"}
        )


#CUSTOMER 

class CustomerListCreateView(APIView):

    def get(self, request):

        qs = CustomerDb.objects.all()

        serializer_instance = CustomerSerializer(
            qs,
            many=True
        )

        return Response(data=serializer_instance.data)

    def post(self, request):

        form_data = request.data

        serializer_instance = CustomerSerializer(
            data=form_data
        )

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(
                data=serializer_instance.data
            )

        else:

            return Response(
                data=serializer_instance.errors
            )


class CustomerRetrieveUpdateDeleteView(APIView):

    def get(self, request, pk):

        qs = get_object_or_404(
            CustomerDb,
            id=pk
        )

        serializer_instance = CustomerSerializer(qs)

        return Response(
            data=serializer_instance.data
        )

    def put(self, request, pk):

        form_data = request.data

        customer_object = get_object_or_404(
            CustomerDb,
            id=pk
        )

        serializer_instance = CustomerSerializer(
            data=form_data,
            instance=customer_object
        )

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(
                data=serializer_instance.data
            )

        else:

            return Response(
                data=serializer_instance.errors
            )

    def delete(self, request, pk):

        customer_object = get_object_or_404(
            CustomerDb,
            id=pk
        )

        customer_object.delete()

        return Response(
            data={"message": "Deleted...!"}
        )


# ---------------- BOOKING ----------------

class BookingListCreateView(APIView):

    def get(self, request):

        qs = BookingDb.objects.all()

        serializer_instance = BookingSerializer(
            qs,
            many=True
        )

        return Response(
            data=serializer_instance.data
        )

    def post(self, request):

        form_data = request.data

        serializer_instance = BookingSerializer(
            data=form_data
        )

        if serializer_instance.is_valid():

            hotel = serializer_instance.validated_data.get("hotel")
            check_in = serializer_instance.validated_data.get("check_in")
            check_out = serializer_instance.validated_data.get("check_out")

            # Calculate number of days
            duration = check_out - check_in
            number_of_days = duration.days

            # Calculate total amount
            total_amount = (
                hotel.price_per_day *
                Decimal(number_of_days)
            )

            form_data["total_amount"] = total_amount

            booking_object = BookingDb.objects.create(
                **form_data
            )

            serializer_instance = BookingSerializer(
                booking_object
            )

            return Response(
                data={
                    "message": "Booking successful..!",
                    "data": serializer_instance.data
                }
            )

        else:

            return Response(
                data=serializer_instance.errors
            )


class BookingRetrieveUpdateDeleteView(APIView):

    def get(self, request, pk):

        qs = get_object_or_404(
            BookingDb,
            id=pk
        )

        serializer_instance = BookingSerializer(qs)

        return Response(
            data=serializer_instance.data
        )

    def put(self, request, pk):

        form_data = request.data

        booking_object = get_object_or_404(
            BookingDb,
            id=pk
        )

        serializer_instance = BookingSerializer(
            data=form_data,
            instance=booking_object
        )

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(
                data=serializer_instance.data
            )

        else:

            return Response(
                data=serializer_instance.errors
            )

    def delete(self, request, pk):

        booking_object = get_object_or_404(
            BookingDb,
            id=pk
        )

        booking_object.delete()

        return Response(
            data={"message": "Deleted...!"}
        )