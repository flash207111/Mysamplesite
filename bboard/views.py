from django.shortcuts import render
# from django.http import HttpResponse
from .models import Bb

def index(request):
    # queryset = Bb.objects.order_by('-published') # list of objects
    queryset = Bb.objects.all() # list of objects
    context = {
        'object_list': queryset
    }
    return render(request, 'bboard/index.html', context)

