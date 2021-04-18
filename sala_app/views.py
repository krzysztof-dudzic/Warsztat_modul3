from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from sala_app.models import *

def index(request):

    return render(request, 'start_page.html')


class AddRoom(View):
    def get(self, request):
        return render(request, template_name="add_room.html")

    def post(self, request):
        name = request.POST.get('name')
        capacity = request.POST.get('capacity')
        projector = request.POST.get('capacity')
        name_a = Room.objects.all()
        if name == '':
            return HttpResponse("Name of room is empty")
        else:
            if name in name_a:
                return HttpResponse("This name already exists")
            else:
                capacity_a = int(capacity)
                if capacity_a < 0:
                    return HttpResponse("This room is not capacity")
                else:
                    return render(request, template_name="add_room.html",
                                  context={"name": name, "capacity": capacity, "projector": projector})


