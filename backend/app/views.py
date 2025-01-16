from .models import Room, Booking
from .serializers import RoomSerializer, BookingSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# for admin
@api_view(['GET', 'POST'])  # Allows both GET and POST methods for this route
def room_list(request):
    if request.method == 'GET':
        rooms = Room.objects.all()  # Get all rooms
        serializer = RoomSerializer(rooms, many=True)  # Serialize rooms
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RoomSerializer(data=request.data)  # Serialize the incoming data for room creation
        if serializer.is_valid():
            serializer.save()  # Save the new room
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def room_update(request, room_id):
    try:
        room = Room.objects.get(id=room_id)
    except Room.DoesNotExist:
        return Response({"error": "Room not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = RoomSerializer(room, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def room_delete(request, room_id):
    try:
        room = Room.objects.get(id=room_id)
    except Room.DoesNotExist:
        return Response({"error": "Room not found"}, status=status.HTTP_404_NOT_FOUND)

    room.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# user view
@api_view(['GET'])
def available_room_list(request):
    available_rooms = Room.objects.filter(is_available=True)
    serializer = RoomSerializer(available_rooms, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def book_room(request):
    serializer = BookingSerializer(data=request.data)
    if serializer.is_valid():
        booking=serializer.save()
        booking.room.is_available=False
        booking.room.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def cancel_booking(request, booking_id):
    try:
        booking = Booking.objects.get(id=booking_id)
    except Booking.DoesNotExist:
        return Response({"error": "Booking not found"}, status=status.HTTP_404_NOT_FOUND)

    booking.is_cancelled = True
    booking.room.is_available = True
    booking.room.save()
    booking.save()
    return Response(status=status.HTTP_204_NO_CONTENT)

