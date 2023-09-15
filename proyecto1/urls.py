"""
URL configuration for proyecto1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from App_tienda import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.inicio,name='inicio'),
    path('empleados',views.empleados,name='empleados'),
    path('productos',views.productos,name='productos'),
    path('proveedores',views.proveedores,name='proveedores'),
    path('productos/agregar',views.agregar,name='agregar'),
    path('productos/borrar/<int:id>',views.borrar,name='borrar'),
    path('productos/detalle/<int:id>',views.detalle,name='detalle'), #Para mostrar el formulario 
    path('productos/editar',views.editar,name='editar'),#Para editar producto mediante el formulario
    
    path('empleado/detalle1/<int:id>',views.detalle1,name='detalle1'), #Para mostrar el formulario 
    path('empleado/editar1',views.editar1,name='editar1'),#Para editar empleado mediante el formulario
    path('empleados/guardar1',views.guardar1,name='guardar1'),
    path('empleados/eliminar1/<int:id>',views.eliminar1,name='eliminar1'),

    path('proveedor/detalle2/<int:id>',views.detalle2,name='detalle2'),
    path('proveedor/editar2',views.editar2,name='editar2'),
    path('proveedores/guardar',views.guardar,name='guardar'),
    path('proveedores/eliminar/<int:id>',views.eliminar,name='eliminar'),
  



]
