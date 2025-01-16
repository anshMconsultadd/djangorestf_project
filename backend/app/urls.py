from django.urls import path
from .views import (
    room_list,
    room_update,
    room_delete,
    available_room_list,
    book_room,
    cancel_booking
)

urlpatterns = [

    path('admin/rooms/', room_list, name='view_rooms'),
    path('admin/rooms/<int:room_id>/', room_update, name='update_room'),
    path('admin/rooms/<int:room_id>/delete/', room_delete, name='delete_room'),

    path('rooms/', available_room_list, name='search_rooms'),
    path('rooms/book/', book_room, name='book_room'),
    path('rooms/cancel/', cancel_booking, name='cancel_booking'),
]