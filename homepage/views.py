from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.template import loader
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect
from .forms import ContatoModelForm
from .models import Contato

def index(request):
    if str(request.method) == 'POST':
        form = ContatoModelForm(request.POST, request.FILES)
        if form.is_valid():

            form.save()

            messages.success(request, 'Contato salvo com sucesso.')
            form = ContatoModelForm()
        else:
            messages.error(request, 'Erro ao salvar Contato.')
    else:
        form = ContatoModelForm()
    context = {
        'form': form
    }
    return render(request, 'index.html', context)

def error404(request,Exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)


def error500(request, Exception):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)

def contato(request):
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            form = ContatoModelForm(request.POST, request.FILES)
            if form.is_valid():

                form.save()

                messages.success(request, 'Contato salvo com sucesso.')
                form = ContatoModelForm()
            else:
                messages.error(request, 'Erro ao salvar Contato.')
        else:
            form = ContatoModelForm()
        context = {
            'form': form
        }
        return render(request, 'contato.html', context)
    else:
        return redirect('index')