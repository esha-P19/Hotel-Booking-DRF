from django.db import models


class HotelDb(models.Model):
    hotel_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField()
    room_type = models.CharField(max_length=100)
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.hotel_name


class CustomerDb(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class BookingDb(models.Model):
    hotel = models.ForeignKey(HotelDb, on_delete=models.CASCADE)
    customer = models.ForeignKey(CustomerDb, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.customer} - {self.hotel}"