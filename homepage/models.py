from django.db import models
from django.db.models import signals
from django.template.defaultfilters import slugify


class Base(models.Model):
    criado = models.DateField('Data de criação', auto_now_add=True)
    modificado = models.DateField('Data de atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

class Contato(Base):
    nome = models.CharField('nome', max_length=100)
    email = models.EmailField('email', max_length=100)
    mensagem = models.TextField('mensagem')
    slug = models.SlugField('slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.nome
def contato_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)

signals.pre_save.connect(contato_pre_save, sender=Contato)