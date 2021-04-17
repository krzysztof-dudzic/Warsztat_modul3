from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


def index(request):

    return render(request, 'start_page.html')



class AddRoom(View):
    def get(self, request):
        return render(request, template_name="add_room.html")

    def post(self, request):
        name = request.POST.get('name')
        capacity = request.POST.get('capacity')
        projector = request.POST.get('capacity')
        if name == '':
            return HttpResponse("Name of room is empty")
        else:
            if name:
                return HttpResponse("This name already exists")
            else:
                if capacity < 0:
                    return HttpResponse("This room is not capacity")
                else:
                    return render(request, template_name="add_room.html",
                                  context={"name": name, "capacity": capacity, "projector": projector})


