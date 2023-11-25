from django import forms


class ChoiceForm(forms.Form):
    choice_text = forms.CharField(max_length=100, label="Nome Escolha")


class QuestionForm(forms.Form):
    question_text = forms.CharField(max_length=100, label="Questão")
    teste = forms.IntegerField(label="Teste")


class DadosMetereologicosForm(forms.Form):
    temperatura = forms.IntegerField()
    umidade = forms.DecimalField()


class RegiaoForm(forms.Form):
    regiao = forms.CharField(max_length=100)
    cidade = forms.CharField(max_length=100)


class CadastoForm(forms.Form):
    nome = forms.CharField(max_length=100, label="Nome",
                           widget=forms.TextInput(attrs={"placeholder": "Nome"}))
    email = forms.CharField(max_length=100, label="Email",
                            widget=forms.TextInput(attrs={"placeholder": "Email"}))
    senha = forms.CharField(max_length=100, label="Senha",
                            widget=forms.TextInput(attrs={"placeholder": "Senha", "type": "password", "minlength": "8"}))


class ValidaLoginForm(forms.Form):
    email = forms.CharField(max_length=100, label="Email",
                            widget=forms.TextInput(attrs={"placeholder": "Email"}))
    senha = forms.CharField(max_length=100, label="Senha",
                            widget=forms.TextInput(attrs={"placeholder": "Senha", "type": "password", "minlength": "8"}))
