from django.shortcuts import render
from datetime import date
from datetime import datetime
from .models import Simulacao

def index(request):
    #parcelas = [1,2]
    #taxas = [6%,8%]
    return render(request, 'simular/index.html', {})


def simulacao(request):
    if request.POST:
        nome = request.POST.get('nome')    
        telefone = request.POST.get('telefone')    
        email = request.POST.get('email')       
        valor = int(request.POST.get('valor')) + 0.01
        valor =  round(valor, 2)
        parcelas = request.POST.get('parcelas')
        valorpagar = 0
        data = datetime.now()
        #data = data.strftime('%d/%m/%Y')
        
        conveniencia = 0.1
        
        if parcelas == '1':
            valorpagar = valor+(valor*0.06)
        elif parcelas == '2':
            valorpagar = valor+(valor*0.08)
        elif parcelas == '3':
            valorpagar = valor+(valor*0.1)
        
        valorpagar = valorpagar+(valorpagar*conveniencia)
        valorpagar = round(valorpagar, 2)
    
        create = Simulacao.objects.create(nome=nome,telefone=telefone,email=email,valor=valor,parcelas=parcelas,data=data,valorfinal=valorpagar)
        create.save()
    
    return render(request, 'simular/simulacao.html', {'nome':nome,'email':email,'data':data, 'valorpagar':valorpagar, 'telefone': telefone, 'valor':valor, 'parcelas':parcelas})