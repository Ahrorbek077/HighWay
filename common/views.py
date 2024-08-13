from django.views.generic import View
from django.views.generic import DetailView, ListView
from django.shortcuts import render

from common import models

class HomeView(View):
    def get(self, request):
        videos = models.Video.objects.all()
        galleries = models.Gallery.objects.all()

        context = {
            'videos': videos,
            'galleries': galleries
        }
        return render(request, "index.html", context)


