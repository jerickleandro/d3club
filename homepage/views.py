from django.shortcuts import render

from django.shortcuts import get_object_or_404

from django.http import HttpResponse
from django.template import loader

def index(request):
    context = {
        'mensagem': 'Essa é a pagina inicial do D3Club'
    }
    return render(request, 'index.html', context)

def error404(request,ex):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)


def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)