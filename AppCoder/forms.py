from django import forms


class MascotaFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    edad = forms.IntegerField()


class ProfesionFormulario(forms.Form):   
    nombre= forms.CharField(max_length=200)
