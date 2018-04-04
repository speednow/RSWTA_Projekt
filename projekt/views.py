from django.shortcuts import render
from django.utils import timezone
from .models import Firma
from .models import Oferta

def oferta_list(request):
    oferta = Oferta.objects.filter(data_utworzenia__lte=timezone.now()).order_by('data_utworzenia')
    return render(request, 'projekt/oferta_list.html', {'oferta': oferta})
# Create your views here.
