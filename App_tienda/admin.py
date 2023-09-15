from django.contrib import admin
from App_tienda.models import Proveedores,Productos
from App_tienda.models import Empleados,Seccion


# Register your models here.

admin.site.register(Proveedores)
admin.site.register(Productos)
admin.site.register(Empleados)
admin.site.register(Seccion)
