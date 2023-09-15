from django.shortcuts import render,redirect
from App_tienda.models import Productos,Empleados
from App_tienda.models import Proveedores
from django.contrib import messages



# Definir las funcciones para cada plantilla.

def inicio(request):
    return render(request,'inicio.html')

#Listar todos los productos en la base de datos
def productos(request):
    productos = Productos.objects.all()
    return render(request,'productos.html',{'clave1':productos})# usamos una clave y un valor para listar los datos

#Agregar productos 
def agregar(request):
    n = request.POST['nombre']
    p = request.POST['precio']
    desc = request.POST['descripcion']
    producto1 = Productos(nombre=n,precio=p,descripcion=desc)
    producto1.save()
    messages.success(request,'Agregaste un producto')
    return redirect('productos')

#Eliminar producto 
def borrar(request,id):
 producto = Productos.objects.filter(pk=id)
 producto.delete()
 messages.success(request,'Elimnaste un producto')
 return redirect('productos')

#Mostrar el fomulario de producto 
def detalle(request,id):
   producto = Productos.objects.get(pk=id)
   return render(request,"editarProducto.html",{'producto': producto})

#Editar productos 
def editar(request):
    nombre = request.POST["nombre"]
    precio = request.POST["precio"]
    descripcion = request.POST["descripcion"]
    id = request.POST["id"]
    Productos.objects.filter(pk=id).update(id=id,nombre=nombre,precio=precio,descripcion=descripcion)
    messages.success(request,'Producto actualizado')
    return redirect('productos')


#########################################

#Listar todos los empleados 
def empleados(request):
    empleados = Empleados.objects.all()
    return render(request,'empleados.html',{'clave3':empleados})

#Agregar empleador
def guardar1(request):
    nom = request.POST["nombre"]
    ape = request.POST["apellido"]
    dir = request.POST["direccion"]
    tel = request.POST["telefono"]
    empleado1 = Empleados(nombre=nom,apellido=ape,direccion=dir,telefono=tel)
    empleado1.save()
    messages.success(request,'Agregaste un empleado')
    return redirect('empleados')

#Eliminar empleador  
def eliminar1(request,id):
 empleado = Empleados.objects.filter(pk=id)
 empleado.delete()
 messages.success(request,'Elimnaste un empleado')
 return redirect('empleados') 

#Mostrar el fomulario de empleado 
def detalle1(request,id):
   empleado = Empleados.objects.get(pk=id)
   return render(request,"editarEmpleado.html",{'empleado': empleado})

#Editar empleado 
def editar1(request):
    nombre = request.POST["nombre"]
    apellido = request.POST["apellido"]
    direccion = request.POST["direccion"]
    telefono = request.POST["telefono"]
    id = request.POST["id"]
    Empleados.objects.filter(pk=id).update(id=id,nombre=nombre,apellido=apellido,direccion=direccion,telefono=telefono)
    messages.success(request,'Empleado actualizado')
    return redirect('empleados')


######################################

#Listar proveedores 
def proveedores(request):
    proveedores = Proveedores.objects.all()
    return render(request,'proveedores.html',{'clave2':proveedores})

#Agregar proveedor
def guardar(request):
    nom = request.POST["nombre"]
    ape = request.POST["apellido"]
    dir = request.POST["direccion"]
    tel = request.POST["telefono"]
    proveedor1 = Proveedores(nombre=nom,apellido=ape,direccion=dir,telefono=tel)
    proveedor1.save()
    messages.success(request,'Agregaste un proveedor')
    return redirect('proveedores')

#Eliminar proveedor  
def eliminar(request,id):
 proveedor = Proveedores.objects.filter(pk=id)
 proveedor.delete()
 messages.success(request,'Elimnaste un proveedor')
 return redirect('proveedores') 

#Mostrar el fomulario de proveedor 
def detalle2(request,id):
   proveedor = Proveedores.objects.get(pk=id)
   return render(request,"editarProveedor.html",{'proveedor': proveedor})

#Editar proveedor 
def editar2(request):
    nombre = request.POST["nombre"]
    apellido = request.POST["apellido"]
    direccion = request.POST["direccion"]
    telefono = request.POST["telefono"]
    id = request.POST["id"]
    Proveedores.objects.filter(pk=id).update(id=id,nombre=nombre,apellido=apellido,direccion=direccion,telefono=telefono)
    messages.success(request,'Proveedor actualizado')
    return redirect('proveedores')











