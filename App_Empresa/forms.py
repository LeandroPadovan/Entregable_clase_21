from django import forms

class ClienteForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=50)
    apellido = forms.CharField(label="Apellido", max_length=50)
    dni = forms.IntegerField(label="DNI")
    mail = forms.EmailField(label="Email")


class ProveedorForm(forms.Form):
    razon_social = forms.CharField(label = "Razón social" , max_length=50)
    cuit = forms.IntegerField(label="CUIT")
    mail = forms.EmailField(label="Email")
    forma_de_pago = forms.CharField(label="Forma de pago")

class ColaboradorForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=50)
    apellido = forms.CharField(label="Apellido", max_length=50)
    dni = forms.IntegerField(label="DNI")
    mail = forms.EmailField(label="Email")
    area = forms.CharField(label="Area")

