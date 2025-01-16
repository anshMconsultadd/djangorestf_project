from django.db import models

class Room(models.Model):
    room_number = models.CharField(max_length=10)
    room_type = models.CharField(max_length=50)
    capacity = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Room {self.room_number} - {self.room_type}"

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    check_in = models.DateField()
    check_out = models.DateField()
    is_cancelled = models.BooleanField(default=False)

    def __str__(self):
        return f"Booking for {self.user_name} in Room {self.room.room_number}"
