from django.shortcuts import render


def oferta_list(request):
    return render(request, 'projekt/oferta_list.html', {})
# Create your views here.
