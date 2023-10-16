import os
from django.shortcuts import render
from django.views import generic
from .forms import DadosMetereologicosForm, RegiaoForm
from pymongo import MongoClient
from bson import Decimal128
import datetime
import decimal
from bson.objectid import ObjectId
from dotenv import load_dotenv

# Create your views here.

MONGODB_URI = os.environ['MONGODB_URI']
OPTIONS = os.environ['OPTIONS']

client = MongoClient(
    MONGODB_URI+OPTIONS)
db = client.WheatherDB
regiao = db.regiao
dados_metereologicos = db.dados_metereologicos
#  {
#           label: "My First Dataset",
#           data: teste,
#           parsing: {
#             xAxisKey: 'dt_criacao',
#             yAxisKey: 'umidade'
#           }
#  }


def IndexView(request):
    template_name = "theweather/index.html"
    context_object_name = "latest_regiao_list"

    lookup = {"$lookup": {"from": "dados_metereologicos",
                          "localField": "_id",
                          "foreignField": "id_regiao",
                          "as": "dadosM"}}
    project = {"$project": {'_id': 0, 'cidade': 0, 'dadosM._id': 0,
                            'dadosM.id_regiao': 0, 'dadosM.regiao': 0}}

    pipeline = [lookup, project]

    results = list(regiao.aggregate(pipeline))
    print(results)

    resultsFilter = []

    for dados in results:
        for maps in dados['dadosM']:
            for key, value in maps.items():
                if (type(value) == Decimal128):
                    maps[key] = float(str(maps[key]))
                elif (type(value) == datetime.datetime):
                    maps[key] = maps[key].strftime('%d/%m/%y %H:%M:%S')
        resultsFilter.append(dados)

    """Return the last five published questions."""
    return render(request, template_name, {context_object_name: resultsFilter})


def cadastrar_regiao(request):
    form_Regiao = RegiaoForm(request.POST)
    form_Metereologia = DadosMetereologicosForm(request.POST)

    if request.method == 'POST':
        if all([form_Regiao.is_valid(), form_Metereologia.is_valid()]):
            _id = ObjectId()
            input_Regiao = form_Regiao.cleaned_data
            input_Metereologico = form_Metereologia.cleaned_data

            input_Metereologico = {k: (Decimal128(str(v)) if type(
                v) == decimal.Decimal else v) for k, v in input_Metereologico.items()}

            regiao.insert_one({"_id": _id, **input_Regiao})
            dados_metereologicos.insert_one(
                {"id_regiao": _id, **input_Metereologico, "dt_criacao": datetime.datetime.now()})

            # q = Regiao(**teste2,
            #            dados_metereologicos=[DadosMetereologicos(**teste1)])
            # # q.save()

    else:
        form_Regiao = RegiaoForm()
        form_Metereologia = DadosMetereologicosForm()

    return render(request, 'theweather/cadastro.html', {'form': form_Regiao, "form2": form_Metereologia})
