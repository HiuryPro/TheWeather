from django import forms


class ChoiceForm(forms.Form):
    choice_text = forms.CharField(max_length=100, label="Nome Escolha")


class QuestionForm(forms.Form):
    question_text = forms.CharField(max_length=100, label="Questão")
    teste = forms.IntegerField(label="Teste")


class DadosMetereologicosForm(forms.Form):
    temperatura = forms.IntegerField()
    umidade = forms.DecimalField(decimal_places=2)


class RegiaoForm(forms.Form):
    regiao = forms.CharField(max_length=100)
