from django.db import models


# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dni = models.IntegerField()
    mail = models.EmailField()

    def __str__(self):
        return self.nombre + " " + str(self.apellido) + " " + str(self.dni) + " " + str(self.mail) 

class Proveedor(models.Model):
    razon_social = models.CharField(max_length=100)
    cuit = models.IntegerField()
    mail = models.EmailField()
    forma_de_pago = models.CharField(max_length=50)

    def __str__(self):
        return self.razon_social + " " + str(self.cuit) + " " + str(self.mail) + " " + str(self.forma_de_pago) 

class Colaborador(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dni = models.IntegerField()
    mail = models.EmailField()
    area = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre + " " + str(self.apellido) + " " + str(self.dni) + " " + str(self.mail) + " " + str(self.area) 

