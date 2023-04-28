from django.shortcuts import render
from .models import Items
# Create your views here.

def index(request):
    item_dict = {
        'items' : Items.objects.all
    }
    return render(request, 'index.html', item_dict)