from django.shortcuts import render
from .models import SliderIndex, Galeria, MisionyVision,Producto
 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout,login as login_aut
from django.contrib.auth.decorators import login_required, permission_required
import requests
# Create your views here.
def index (request):
    autos = SliderIndex.objects.all()
    return render(request,'web/index.html',{'autos':autos})

def galeria(request):
    autos = Galeria.objects.all()
    return render(request,'web/galeria.html',{'autos':autos})

def formulario(request):
    if request.POST:
        nombre = request.POST.get("txtNombre")
        apellido = request.POST.get("txtApellido")
        email = request.POST.get("txtEmail")
        pass1= request.POST.get("txtContraseña")
        pass2= request.POST.get("txtContraseña2")
        usuario= request.POST.get("txtUsuario")

        if pass1 != pass2:
            return render(request, 'web/formulario.html',{'msg':'Las contraseñas no coinciden'})
        try:
            usu=User.objects.get(username=usuario)
            return render(request, 'web/formulario.html',{'msg':'usuario existe'})

        except: 
            usu= User()
            usu.first_name=nombre
            usu.last_name=apellido
            usu.email=email
            usu.set_password(pass1)
            usu.username=usuario
            usu.save()
            us = authenticate(request, username=usuario, password=pass1)
            login_aut(request,us)

            autos = SliderIndex.objects.all()
            return render(request,'web/index.html',{'autos':autos})

    return render(request, 'web/formulario.html')


@login_required(login_url='/login')
@permission_required('lavado.delete_producto',login_url='/login')
def eliminar(request,id):
    try:
        producto = Producto.objects.get(nombre=id)
        producto.delete()
        msg='eliminó producto'
    except:
        msg='no eliminó insumo'
    producto = Producto.objects.all()
    return render (request,'web/admin_producto.html',{'lista_producto':producto, 'msg':msg})

@login_required(login_url='/login')
@permission_required('lavado.view_producto',login_url='/login')
def busqueda_prod(request,id):
    try:
        producto = Producto.objects.get(nombre=id)
        return render(request,'web/producto_mod.html',{'producto':producto})
    except:
        msg='no se modificó'
    producto = Producto.objects.all()
    return render (request,'web/admin_producto.html',{'lista_producto':producto, 'msg':msg})

@login_required(login_url='/login')
@permission_required('lavado.view_producto',login_url='/login')
@permission_required('lavado.change_producto',login_url='/login')
def modificar(request):
    if request.POST:
        nombre = request.POST.get('txtNombre')
        precio = request.POST.get('txtPrecio')
        descripcion = request.POST.get('txtDescripcion')
        stock = request.POST.get('txtStock')
        try:
            producto= Producto.objects.get(nombre=nombre)
            producto.precio = precio
            producto.descripcion = descripcion
            producto.stock=stock
            producto.save()
            msg='modifico'
        except:
            msg='no modifico'
    producto = Producto.objects.all()
    return render (request,'web/admin_producto.html',{'lista_producto':producto,'msg':msg})
  



@login_required(login_url='/login')
@permission_required('lavado.view_producto',login_url='/login')
def lista_producto(request):
    # producto = Producto.objects.all()
    response = requests.get("http://localhost:8000/api/insumos/")
    producto = response.json()
    return render (request,'web/admin_producto.html',{'lista_producto':producto})

@login_required(login_url='/login')
@permission_required('lavado.add_producto',login_url='/login')
def producto(request):
    if request.POST:
        nombre = request.POST.get('txtNombre')
        precio = request.POST.get('txtPrecio')
        descripcion = request.POST.get('txtDescripcion')
        stock = request.POST.get('txtStock')

        datos_json ={
            "nombre":nombre,
            "precio":precio,
            "descripcion":descripcion,
            "stock":stock
        }
        response = requests.post("http://localhost:8000/api/insumos/",data=datos_json)
        return render(request, 'web/producto.html',{'msg':'Grabó producto'})


    return render(request, 'web/producto.html')

def quienes(request):
    myv = MisionyVision.objects.all()
    return render(request, 'web/quienes_somos.html',{'myv':myv})

def servicios(request):
    return render (request, 'web/servicios.html')

def cerrar_sesion(request):
    logout(request)
    autos = SliderIndex.objects.all()
    return render(request,'web/index.html',{'autos':autos})         

def login(request):
    if request.POST:
        usuario = request.POST.get('txtUser')
        password = request.POST.get('txtContraseña')
        us = authenticate(request, username=usuario, password=password)
        if us is not None and us.is_active:
            login_aut(request,us)
            autos = SliderIndex.objects.all()
            return render(request,'web/index.html',{'autos':autos})     
        else:
            return render (request, 'web/login.html',{'msg':'usuario o contraseña no coinciden con ninguna cuenta'})
    return render (request, 'web/login.html')