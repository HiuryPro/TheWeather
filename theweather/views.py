from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import DadosMetereologicos, Regiao
from django.utils import timezone
from .forms import DadosMetereologicosForm, RegiaoForm

# Create your views here.


class IndexView(generic.ListView):
    template_name = "theweather/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Regiao.objects


def cadastrar_regiao(request):
    form = RegiaoForm(request.POST)
    formset = DadosMetereologicosForm(request.POST)
    if request.method == 'POST':
        if all([form.is_valid(), formset.is_valid()]):
            print('corno')
            teste2 = form.cleaned_data
            teste1 = formset.cleaned_data
            q = Regiao(**teste2,
                       dados_metereologicos=[DadosMetereologicos(**teste1)])
            q.save()

            print(teste2, teste1)
    else:
        form = RegiaoForm()
        formset = DadosMetereologicosForm()

    return render(request, 'theweather/cadastro.html', {'form': form, "form2": formset})


class DetailView(generic.DetailView):
    model = Regiao
    template_name = "polls/detail.html"
