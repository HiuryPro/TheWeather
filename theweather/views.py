import os
from django.shortcuts import render
from django.views import generic
from .forms import DadosMetereologicosForm, RegiaoForm
from pymongo import MongoClient
from bson import Decimal128
import datetime
import decimal

# Create your views here.

MONGODB_URI = os.environ['MONGODB_URI']
client = MongoClient(MONGODB_URI)
db = client.WheatherDB
regiao = db.regiao


class IndexView(generic.ListView):
    template_name = "theweather/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):

        results = list(regiao.find())

        """Return the last five published questions."""
        return results


def cadastrar_regiao(request):
    form_Regiao = RegiaoForm(request.POST)
    form_Metereologia = DadosMetereologicosForm(request.POST)
    
    if request.method == 'POST':
        if all([form_Regiao.is_valid(), form_Metereologia.is_valid()]):

            input_Regiao = form_Regiao.cleaned_data
            input_Metereologico = form_Metereologia.cleaned_data

            input_Metereologico = {k: (Decimal128(str(v)) if type(
                v) == decimal.Decimal else v) for k, v in input_Metereologico.items()}

            insert_RegiaoMetereologica = {**input_Regiao, "dados_metereologicos": [
                {**input_Metereologico, "dt_criacao": datetime.datetime.now()}]}

            print(insert_RegiaoMetereologica)

            regiao.insert_one(insert_RegiaoMetereologica)

            # q = Regiao(**teste2,
            #            dados_metereologicos=[DadosMetereologicos(**teste1)])
            # # q.save()

    else:
        form_Regiao = RegiaoForm()
        form_Metereologia = DadosMetereologicosForm()

    return render(request, 'theweather/cadastro.html', {'form': form_Regiao, "form2": form_Metereologia})
