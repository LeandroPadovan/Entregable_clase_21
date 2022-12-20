from django.urls import path
from App_Empresa.views import * 
from App_Empresa.Template import *


urlpatterns = [
   
   path("clienteform/", clienteform , name="ClienteForm" ),
   path("proveedorform/", proveedorform , name = "ProveedorForm" ),
   path("colaboradorform/", colaboradorform , name = "ColaboradorForm"),
   path("buscarcliente/", clientebusqueda , name = "ClienteBusqueda"),
   path("buscarc/", buscarcliente , name="Buscarc"),
   path("buscarproveedor/", proveedorbusqueda , name = "ProveedorBusqueda"),
   path("buscarp/", buscarproveedor , name = "BuscarProveedor"), 
   path("buscarcol/" , buscarcolaborador , name = "BuscarColaborador"),
   path("buscarcolaborador/" , colaboradorbusqueda , name = "ColaboradorBusqueda"),
   path("confirmacion/", confirmacion ),
   
   
]






