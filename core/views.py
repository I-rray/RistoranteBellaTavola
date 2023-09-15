from django.http import Http404
from django.shortcuts import render, redirect
from .models import Usuario, Noticia, Resena_Switch, Resena_Xbox, Resena_Play, About
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import logout
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

def registro_usuario(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        nombre_usuario = request.POST['nombre_usuario']
        email = request.POST['email']
        contrasena = request.POST['contrasena']
        fecha_nacimiento = request.POST['fecha-nacimiento']
        direccion_despacho = request.POST['despacho']
        usuario = Usuario(nombre=nombre, nombre_usuario=nombre_usuario, email=email, contrasena=contrasena, fecha_nacimiento=fecha_nacimiento, direccion_despacho=direccion_despacho)
        usuario.save()
        return redirect('registrar')
    else:
        return render(request, 'core/registrar.html')
    
@csrf_protect
def inicio_sesion(request):
    if request.method == 'POST':
        # Obtenemos el email y la contraseña del formulario
        email = request.POST.get('email')
        contrasena = request.POST.get('contrasena')
        usuario = Usuario.objects.filter(email=email, contrasena=contrasena).first()
        if usuario is not None:
            nombre_usuario = usuario.nombre_usuario
            request.session['nombre'] = usuario.nombre
            request.session['nombre_usuario'] = usuario.nombre_usuario
            request.session['email'] = usuario.email
            fecha_nacimiento_str = usuario.fecha_nacimiento.strftime('%d/%m/%Y')
            request.session['fecha_nacimiento'] = fecha_nacimiento_str
            request.session['direccion_despacho'] = usuario.direccion_despacho
            request.session['nombre_usuario'] = nombre_usuario
            request.session['is_authenticated'] = True

            # Mostramos la alerta solo si no se ha mostrado antes
            if 'alerta_mostrada' not in request.session:
                request.session['alerta_mostrada'] = True
                return render(request, 'core/home.html', {'nombre_usuario': nombre_usuario, 'mostrar_alerta': True})
            else:
                return render(request, 'core/home.html', {'nombre_usuario': nombre_usuario})

        else:
            # Credenciales incorrectas
            return render(request, 'core/login.html', {'error': 'Correo electrónico o contraseña incorrectos.'})
    else:
        # Método GET, mostramos la página de inicio de sesión
        return render(request, 'core/login.html')
    
def logout_view(request):
    request.session['is_authenticated'] = False
    logout(request)
    return redirect('login')

@csrf_protect
def password_reset(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            usuario = Usuario.objects.get(email=email)
            contrasena = usuario.contrasena
            return render(request, 'core/recuperasPass.html', {'contrasena': contrasena})
        except ObjectDoesNotExist:
            messages.error(request, 'El correo electrónico ingresado no está registrado en el sistema.')
    
    return render(request, 'core/recuperasPass.html')


@login_required
def perfil_usuario(request):
    usuario = request.user
    return render(request, 'perfilUsuario.html', {'usuario': usuario})

def editar_perfil(request):
    if request.method == 'POST':
        usuario = Usuario.objects.get(nombre_usuario=request.session['nombre_usuario'])
        usuario.nombre = request.POST['nombre']
        usuario.email = request.POST['email']
        usuario.fecha_nacimiento = request.POST['fecha_nacimiento']
        usuario.direccion_despacho = request.POST['direccion_despacho']
        usuario.save()
        request.session['nombre'] = usuario.nombre
        request.session['email'] = usuario.email
        request.session['fecha_nacimiento'] = usuario.fecha_nacimiento
        request.session['direccion_despacho'] = usuario.direccion_despacho
        return redirect('perfilUsuario')
    else:
        usuario = Usuario.objects.get(nombre_usuario=request.session['nombre_usuario'])
        context = {
            'nombre': usuario.nombre,
            'nombre_usuario': usuario.nombre_usuario,
            'email': usuario.email,
            'fecha_nacimiento': usuario.fecha_nacimiento,
            'direccion_despacho': usuario.direccion_despacho,
        }
        return render(request, 'core/perfilUsuario.html', context)






# Create your views here.
def home(request):
    return render(request,'core/home.html')

def registrar(request):
    return render(request, 'core/registrar.html')

def login(request):
    return render(request,'core/login.html')

def recuperasPass(request):
    return render(request, 'core/recuperasPass.html')

def perfilUsuario(request):
    return render(request, 'core/perfilUsuario.html')

def news(request):
    noticias = Noticia.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(noticias, 2)
        noticias = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity': noticias,
        'paginator': paginator
    }
    return render(request, 'core/news.html', data)

def resena(request):
    return render(request, 'core/resena.html')

def resenaSwitch(request):
    resenas_switch = Resena_Switch.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(resenas_switch, 2)
        resenas_switch = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity': resenas_switch,
        'paginator': paginator
    }
    return render(request, 'core/resenaSwitch.html', data)

def resenaXbox(request):
    resenas_xbox = Resena_Xbox.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(resenas_xbox, 2)
        resenas_xbox = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity': resenas_xbox,
        'paginator': paginator
    }
    return render(request, 'core/resenaXbox.html', data)

def resenaPlay(request):
    resenas_play = Resena_Play.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(resenas_play, 2)
        resenas_play = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity': resenas_play,
        'paginator': paginator
    }
    return render(request, 'core/resenaPlay.html', data)

def listarNoticia(request):
    return render(request, 'core/listarNoticia.html')

def about(request):
    about = About.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(about, 2)
        about = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity': about,
        'paginator': paginator
    }
    return render(request, 'core/about.html', data)