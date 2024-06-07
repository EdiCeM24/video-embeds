from django.shortcuts import render
from .models import Video


def home(request):
    pile = Video.objects.all()
    return render(request, 'app/index.html', {'pile':pile})

