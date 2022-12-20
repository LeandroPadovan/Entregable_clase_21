from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.

def cliente(request):
   
    cliente1 = Cliente( nombre = "Prueba" , apellido = "Prueba1" , dni = 12345678 , mail= "prueba@prueba.com")
   
    cliente1.save()
    
    return render(request,"App_Empresa/Cliente.html", {"cliente": cliente1})



def proveedor(request):
   
    proveedor1 = Proveedor( razon_social = "EmpresaX" , cuit = 12345678 , mail= "empresa@prueba.com" , forma_de_pago = "Cuenta Corriente")
   
    proveedor1.save()
    
    return render(request,"App_Empresa/Proveedor.html", {"proveedor": proveedor1})



def colaborador(request):
   
    colaborador1 = Colaborador( nombre = "juan" , apellido = "Perez" , dni = 36707307 , mail= "colab@prueba.com" , area = "Tesoreria")
   
    colaborador1.save()
    
    return render(request,"App_Empresa/Colaborador.html", {"colaborador": colaborador1})


""" def clienteForm(request):
    
    if request.method == "POST":
        nombre = request.POST["Nombre"]
        apellido = request.POST["Apellido"]
        dni = request.POST["DNI"]
        mail = request.POST["Email"]
        cliente1 = Cliente( nombre = nombre, apellido = apellido , dni = dni , mail = mail)
        cliente1.save()
        return render(request, "App_Empresa/Inicio.html", {"mensaje": "Cliente guardado"})

    else:
        return render(request, "App_Empresa/ClienteForm.html") """  


def confirmacion(request):
    return render(request, "App_Empresa/Confirmacion.html")


def clienteform(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            nombre = informacion["nombre"]
            apellido = informacion["apellido"]
            dni = informacion["dni"]
            mail = informacion["mail"]
            cliente = Cliente(nombre = nombre , apellido = apellido , dni = dni , mail = mail)
            cliente.save()
            return render(request, "App_Empresa/Confirmacion.html", { "mensaje": "Cliente guardado correctamente"})
        else:
            return render(request, "App_Empresa/ClienteForm.html", {"form" : form , "mensaje" : "Informacion no válida."})


    else:
        formulario = ClienteForm() 
        return render (request, "App_Empresa/ClienteForm.html", {"form": formulario})



def proveedorform(request):
    if request.method == "POST":
        form = ProveedorForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            razon_social = informacion["razon_social"]
            cuit = informacion["cuit"]
            mail = informacion["mail"]
            forma_de_pago= informacion["forma_de_pago"]
            proveedor = Proveedor(razon_social = razon_social , cuit = cuit , forma_de_pago = forma_de_pago , mail = mail)
            proveedor.save()
            return render(request, "App_Empresa/Confirmacion.html", { "mensaje": "Proveedor guardado correctamente"})
        else:
            return render(request, "App_Empresa/ProveedorForm.html", {"form" : form , "mensaje" : "Informacion no válida."})


    else:
        formulario = ProveedorForm() 
        return render (request, "App_Empresa/ProveedorForm.html", {"form": formulario})




def colaboradorform(request):
    if request.method == "POST":
        form = ColaboradorForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            nombre = informacion["nombre"]
            apellido = informacion["apellido"]
            mail = informacion["mail"]
            dni = informacion["dni"]
            area = informacion["area"]
            colaborador = Colaborador(nombre = nombre , apellido = apellido , dni = dni , mail = mail , area = area)
            colaborador.save()
            return render(request, "App_Empresa/Confirmacion.html", { "mensaje": "Colaborador guardado correctamente"})
        else:
            return render(request, "App_Empresa/ColaboradorForm.html", {"form" : form , "mensaje" : "Informacion no válida."})


    else:
        formulario = ColaboradorForm() 
        return render (request, "App_Empresa/ColaboradorForm.html", {"form": formulario})



def clientebusqueda(request):
   return render(request , "App_Empresa/BusquedaCliente.html")



def buscarcliente(request):

    nombre = request.GET["nombre"]
    apellido = request.GET["apellido"]
    dni = request.GET["dni"]
    mail = request.GET["mail"]


    if nombre or apellido or dni or mail != "": 
        cliente = Cliente.objects.filter(nombre__icontains = nombre, apellido__icontains = apellido , dni__icontains = dni, mail__icontains = mail)
        return render(request, "App_Empresa/ResultadosBusquedaClientes.html", {"cliente": cliente })
    
    else:
        return render(request, "App_Empresa/BusquedaCliente.html", {"mensaje" : "INGRESE UN DATO PARA LA BUSQUEDA"})
    

def proveedorbusqueda(request):
   return render(request , "App_Empresa/BusquedaProveedor.html")


def buscarproveedor(request):

    razon_social = request.GET["razon_social"]
    cuit = request.GET["cuit"]
    mail = request.GET["mail"]
    forma_de_pago = request.GET["forma_de_pago"]

    if razon_social or cuit or mail or forma_de_pago != "":
        proveedor = Proveedor.objects.filter(razon_social__icontains = razon_social , cuit__icontains = cuit , mail__icontains = mail, forma_de_pago__icontains = forma_de_pago)
        return render(request, "App_Empresa/ResultadosBusquedaProveedores.html", {"proveedor": proveedor })
    
    else:
        return render(request, "App_Empresa/BusquedaProveedor.html", {"mensaje" : "INGRESE UN DATO PARA LA BUSQUEDA"}) 



def colaboradorbusqueda(request):
   return render(request , "App_Empresa/BusquedaColaborador.html")



def buscarcolaborador(request):

    nombre = request.GET["nombre"]
    apellido = request.GET["apellido"]
    dni = request.GET["dni"]
    email = request.GET["email"]
    area = request.GET["area"]

    if nombre or apellido or dni or email or area != "":
        colaborador = Colaborador.objects.filter(nombre__icontains = nombre , apellido__icontains = apellido , dni__icontains = dni , mail__icontains = email , area__icontains = area )
        return render(request, "App_Empresa/ResultadosBusquedaColaboradores.html", {"colaborador": colaborador })
    else:
        return render(request, "App_Empresa/BusquedaColaborador.html", {"mensaje" : "INGRESE UN DATO PARA LA BUSQUEDA"}) 

def panel_general(request):
    return render(request , "App_Empresa/Pagina_inicio.html")



