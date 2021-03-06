from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.datetime_safe import datetime
from django.views import View
from sala_app.models import *
import datetime


def index(request):
    return render(request, 'start_page.html')


class AddRoom(View):
    def get(self, request):
        return render(request, template_name="add_room.html")

    def post(self, request):
        name = request.POST.get('name')
        capacity = request.POST.get('capacity')
        projector = request.POST.get('projector') == "on"
        name_rooms = Room.objects.filter(name=name).first()
        if name == '':
            return HttpResponse("Name of room is empty")
        else:
            capacity = int(capacity)
            if name_rooms:
                return HttpResponse("This room exists")
            if capacity <= 0:
                return HttpResponse("This room is not capacity")
            else:
                score = Room(name=name, capacity=capacity, projector=projector)
                score.save()
                return redirect("all-rooms")


class AllRooms(View):
    def get(self, request):
        rooms = Room.objects.all()
        if not rooms:
            return HttpResponse("No available rooms")
        return render(request, template_name='all_room.html', context={'rooms': rooms})


# def view_room(request):
#     rooms = Room.objects.all()
#     return render(request, template_name='view_room.html', context={'rooms': rooms})


# def is_available_room(request):
#     if request.method == 'GET':
#         name = request.GET.get('name')
#         if name:
#             exp = datetime.now() + datetime.timedelta(weeks=52)
#             response = HttpResponse("busy")
#             response.set_cookie(key='busy', value=name.name.encode('utf-8'), expires=exp)
#             return response
#         else:
#             return HttpResponse("Wrong name")

class DeleteRoom(View):
    def get(self, request, room_id):
        room = Room.objects.get(id=room_id)
        room.delete()
        return redirect('all-rooms')


class ModifyRoom(View):
    def get(self, request, room_id):
        room = Room.objects.get(id=room_id)
        return render(request, template_name='modify_room.html', context={'room': room})

    def post(self, request, room_id):
        room = Room.objects.get(id=room_id)
        name = request.POST.get('name')
        capacity = request.POST.get('capacity')
        capacity = int(capacity) if capacity else 0
        projector = request.POST.get('projector') == 'on'
        if name == '':
            return HttpResponse("Brak nazwy sali")
        elif capacity <= 0:
            return HttpResponse("Z??a liczba")
        elif name != room.name and Room.objects.filter(name=name).first():
            return HttpResponse("z??a nazwa")

        room.name = name
        room.capacity = capacity
        room.projector = projector
        room.save()
        return redirect('all-rooms')


class ReserveRoom(View):
    def get(self, request, room_id):
        room = Room.objects.get(id=room_id)
        reservations = room.roomreservation_set.filter(date__gte=str(datetime.date.today())).order_by('date')
        return render(request, template_name="reservation.html", context={'room': room, 'reservations': reservations})

    def post(self, request, room_id):
        room = Room.objects.get(id=room_id)
        date = request.POST.get("date")
        comment = request.POST.get("comment")
        reservations = room.roomreservation_set.filter(date__gte=str(datetime.date.today())).order_by('date')
        if Reserve.objects.filter(room=room, date=date):
            return HttpResponse("Sala jest zaj??ta")
        if date < str(datetime.date.today()):
            return HttpResponse("Z??a data")

        Reserve.objects.create(room=room, date=date, comment=comment)
        return redirect("all-rooms")


class RoomDeatilsView(View):
    def get(self, request, room_id):
        room = Room.objects.get(id=room_id)
        reservations = room.roomreservations_set.filter(date__gte=str(datetime.date().today())).order_by('date')
        return render(request, template_name="details_room.html", context={"room": room, "reservations": reservations})


class RoomListView(View):
    def get(self, request):
        rooms = Room.objects.all()
        for room in rooms:
            reservation_dates = [reservation.date for reservation in room.roomreservation_set.all()]
            room.reserved = datetime.date.today() in reservation_dates
        # reservations = room.roomreservation_set.filter(date__gte=str(datetime.date().today())).order_by('date')
        return render(request, template_name="all_room.html", context={"rooms": rooms})

    # def post(self, request, room_id):
    #     room = Room.objects.get(id=room_id)
    #     date = request.POST.get("date")
    #     comment = request.POST.get("comment")
    #
    #     reservations = room.roomreservation_set.filter(date__gte=str(datetime.date().today())).order_by('date')
    #
    #     if Reserve.objects.filter(room=room, date=date):
    #         return render(request, "reservation.html", context={"room": room,
    #                                                             "reservations": reservations,
    #                                                             "error": "Sala jest ju?? zarezerwowana!"})
    #
    #     if date < str(datetime.date.today()):
    #         return render(request, "reservation.html", context={"room": room,
    #                                                             "reservations": reservations,
    #                                                             "error": "Data jest z przysz??o??ci!"})
    #
    #     Reserve.objects.create(room=room, date=date, comment=comment)
    #     return redirect("all-rooms")


class SearchView(View):
    def get(self, request):
        name = request.GET.get("name")
        capacity = request.GET.get("capacity")
        capacity = int(capacity) if capacity else 0
        projector = request.GET.get("projector") == "on"

        rooms = Room.objects.all()
        if projector:
            rooms = rooms.filter(projector=projector)
        if capacity:
            rooms = rooms.filter(capacity__gte=capacity)
        if name:
            rooms.filter(name__contains=name)

        for room in rooms:
            reservation_dates = [reservation.date for reservation in room.roomreservation_set.all()]
            room.reserved = str(datetime.date.today()) in reservation_dates

        return render(request, template_name="all_room.html", context={"rooms": rooms, "date": datetime.date.today()})







