"""coderslab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from sala_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('room/new/', AddRoom.as_view()),
    path('', index),
    path('list-room/', AllRooms.as_view(), name="all-rooms"),
    # path('/{id}/', view_room),
    path('room/delete/<int:room_id>/', DeleteRoom.as_view(), name="delete-room"),
    path('room/modify/<int:room_id>', ModifyRoom.as_view(), name="modify-rooms"),
    path('room/reserve/<int:room_id>', ReserveRoom.as_view(), name="reserve-room"),
    path('room/<int:room_id>', RoomDeatilsView.as_view(), name="room")



]
