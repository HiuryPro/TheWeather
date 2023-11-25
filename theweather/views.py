import os
from django.shortcuts import render, redirect
from django.views import generic
from .forms import *
from pymongo import MongoClient
from bson import Decimal128
from django.urls import reverse
import datetime
import decimal
from bson.objectid import ObjectId
from dotenv import load_dotenv
from django.contrib import messages
import smtplib
import email.message

# Create your views here.

MONGODB_URI = os.environ['MONGODB_URI']
OPTIONS = os.environ['OPTIONS']

print(MONGODB_URI+OPTIONS)
client = MongoClient(
    MONGODB_URI+OPTIONS)
db = client.WheatherDB
regiao = db.regiao
dados_metereologicos = db.dados_metereologicos
usuario = db.usuario


def IndexView(request):
    template_name = "theweather/index.html"
    context_object_name = "latest_regiao_list"

    lookup = {"$lookup": {"from": "dados_metereologicos",
                          "localField": "_id",
                          "pipeline": [{"$sort": {"dt_criacao": 1}}],
                          "foreignField": "id_regiao",
                          "as": "dadosM"}}

    project = {"$project": {'_id': 0, 'dadosM._id': 0,
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
                    maps[key] = maps[key].strftime('%Y-%m-%d %H:%M:%S')
        resultsFilter.append(dados)

    """Return the last five published questions."""
    return render(request, template_name, {context_object_name: resultsFilter})


def enviar_email(emailname, nome, assunto, corpo):
    corpo_email = f"""
        {nome}
        {corpo}
    """

    msg = email.message.Message()
    msg['Subject'] = assunto
    msg['From'] = 'teagames2023@gmail.com'
    msg['To'] = emailname
    password = 'mjiqlvpsnvbjujot'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')


def testeIndexView(request):
    template_name = "theweather/home.html"
    context_object_name = "latest_regiao_list"

    lookup = {"$lookup": {"from": "dados_metereologicos",
                          "localField": "_id",
                          "pipeline": [{"$sort": {"dt_criacao": -1}}, {"$limit": 1}],
                          "foreignField": "id_regiao",
                          "as": "dadosM"}}

    project = {"$project": {'_id': 0, 'dadosM._id': 0,
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
                    maps[key] = maps[key].strftime('%Y-%d-%m %H:%M:%S')
        resultsFilter.append(dados)

    if request.method == 'POST':
        print(request.POST)
        print(request.POST['nome'])
        enviar_email(request.POST['email'], request.POST['nome'],
                     request.POST['assunto'], request.POST['messagem'])
    return render(request, template_name, {context_object_name: resultsFilter})


def IndexViewCadastrarLogin(request):
    form_Cadastro = CadastoForm()
    template_name = "theweather/cadastro.html"
    print("Cadastrado com Sucesso !")

    if request.method == 'POST':
        form_Cadastro = CadastoForm(request.POST)
        if form_Cadastro.is_valid():
            input_Cadastro = form_Cadastro.cleaned_data
            usuario.insert_one(input_Cadastro)
            print(input_Cadastro)
            messages.success(request, message='Cadastro feito com sucesso!!')
            return redirect(reverse('theweather:IndexViewLogin'))
    else:
        form_Cadastro = CadastoForm()

    """Return the last five published questions."""
    return render(request, template_name,  {'form': form_Cadastro})


def IndexViewLogin(request):
    template_name = "theweather/login.html"
    print("teste")

    if request.method == 'POST':
        form_Login = ValidaLoginForm(request.POST)
        if form_Login.is_valid():
            input_Login = form_Login.cleaned_data
            resultado = usuario.find_one(input_Login)

            if (resultado is not None):
                print("Roteia para Home")
                return redirect(reverse('theweather:home'))
            else:
                print("Email ou senha errado!")
                form_Login = ValidaLoginForm()
                messages.success(request, message='Email ou senha errado!')

            print(input_Login)
            print(resultado)
    else:
        form_Login = ValidaLoginForm()

    """Return the last five published questions."""
    return render(request, template_name,  {'form': form_Login})
