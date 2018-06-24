from django.db import models
from apps.usuarios.models import User
from apps.productos.models import Producto, UnidadMedicion
from django.utils import timezone


class Proveedor(models.Model):
    ruc = models.CharField(max_length=10,primary_key=True)
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Proveedores"

    def __str__(self):
        return self.nombre

class GuiaRemision(models.Model):
    fecha_traslado = models.DateField()
    punto_partida = models.CharField(max_length=30)
    nro_guia_remitente = models.CharField(max_length=15)
    placa_vehiculo = models.CharField(max_length=10)
    licencia_conducir = models.CharField(max_length=15)
    proveedor = models.ForeignKey(Proveedor,blank=True,null=True, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = "Guias de remision"

    def __str__(self):
        return self.nro_guia_remitente

class Almacen(models.Model):
    ubicacion = models.CharField(max_length=50, blank=True, null=True)
    capacidad = models.IntegerField(blank=True,null=True)
    def __str__(self):
        return self.ubicacion
    class Meta:
        verbose_name_plural = "Almacenes"


class Ingreso(models.Model):
    dni_usuario = models.ForeignKey(User, blank=True, null=True, on_delete=models.PROTECT)
    fecha = models.DateField(default=timezone.now ,blank=True, null=True)
    guia_remision = models.ForeignKey(GuiaRemision, blank=True, null=True, on_delete=models.PROTECT)
    tipo = models.IntegerField(blank=True, null=True) #ingreso :1   , reingreso:2
    almacen = models.ForeignKey(Almacen,blank=True,null=True, on_delete=models.PROTECT)
    class Meta:
        verbose_name = "Ingreso"
        verbose_name_plural = "Ingresos"



class DetalleIngreso(models.Model):
    id_ingreso = models.ForeignKey(Ingreso, blank=True, null=True, on_delete=models.PROTECT)
    codigo_producto = models.ForeignKey(Producto, blank=True, null=True, on_delete=models.PROTECT)
    serie = models.CharField(max_length=20, blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    unidad_caja = models.ForeignKey(UnidadMedicion,blank=True, null=True, on_delete=models.PROTECT)
    estado = models.CharField(max_length=15, blank=True, null=True)




class DetalleAlmacen(models.Model):
    codigo_producto = models.ForeignKey(Producto,blank=True,null=True, on_delete=models.PROTECT)
    id_almacen = models.ForeignKey(Almacen,blank=True,null=True, on_delete=models.PROTECT)
    id_ingreso = models.ForeignKey(Ingreso, blank=True, null=True, on_delete=models.PROTECT)
    cantidad = models.IntegerField(blank=True,null=True)
    estado = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        verbose_name = "Detalle de almacen"
        verbose_name_plural = "Detalle de los almacenes"



class Salida(models.Model):
    dni_usuario = models.ForeignKey(User,blank=True,null=True, on_delete=models.PROTECT)
    fecha = models.DateField(blank=True, null=True)
    nodo = models.CharField(max_length=15, blank=True, null=True)
    devolucion = models.NullBooleanField()
    def __str__(self):
        return "Fecha: %s - Nodo: %s" %(self.fecha,self.nodo)
    class Meta:
        verbose_name = "Salida"
        verbose_name_plural = "Salidas"


class DetalleSalida(models.Model):
    id_salida = models.ForeignKey(Salida, blank=True, null=True, on_delete=models.PROTECT)
    id_almacen = models.ForeignKey(Almacen,blank=True, null=True, on_delete=models.PROTECT)
    codigo_producto = models.ForeignKey(Producto,blank=True, null=True, on_delete=models.PROTECT)
    cantidad = models.IntegerField(blank=True, null=True)
    class Meta:
        verbose_name = "Detalles de Salida"
        verbose_name_plural = "Detalles de Salidas"

class DetalleStock(models.Model):
    id_almacen = models.ForeignKey(Almacen,blank=True, null=True, on_delete=models.PROTECT)
    producto = models.ForeignKey(Producto,blank=True, null=True, on_delete=models.PROTECT)
    stock = models.IntegerField(blank=True, null=True)
    class Meta:
        verbose_name = "Stock"
        verbose_name_plural = "Stocks"