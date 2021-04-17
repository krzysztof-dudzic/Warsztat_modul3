from django.shortcuts import render
from django.views import View


class View_room(View):
    def get(self, request):
        return render(request, template_name="add_room.html")

    def post(self, request):


