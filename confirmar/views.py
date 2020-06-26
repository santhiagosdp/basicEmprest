from django.shortcuts import render

def index(request):
    return render(request, 'confirmar/index.html', {})
#   return render(request, 'confirmar/indexm.html', {})