#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, make_response
import time

# importa la carpeta modles
import sys
sys.path.insert(0, './models')
import post #importa lo que hay dentro del archivo post.py
import mantencioncarrera # importa lo que hay dentro del archivo mantencioncarrera.py
import mantencionmediopago # importa lo que hay dentro del archivo mantencionmediopago.py
import mantencionuniversidad # importa lo que hay dentro del archivo mantencionuniversidad.py
import mantenciontipousuario # importa lo que hay dentro del archivo mantenciontipousuario.py
import mantencionpermiso # importa lo que hay dentro del archivo mantencionpermiso.py
import masinfo
import registrousuario # importa lo que hay dentro del archivo registrousuario.py
import login # importa lo que hay dentro del archivo login.py
import mantencionalmuerzo # importa lo que hay dentro del archivo mantencionalmuerzo.py
import registrokiosco
import mostraralmuerzo
import mantencioncategoria
import comment



Post = post.Post()


app = Flask(__name__)#nuevo objeto

app.config['SECRET_KEY'] = '14e69cd065664ebcbb273a07c8105b2e338717fc4786de2479daa8b60d11e3ee9ebf16b80cd04a0ca746164fea8047be6cd76f19ede2ecb75e3ab290beacd472'

## PAGINA PRINCIPAL ##
@app.route('/')#wrap o un decorador
def index():

	#if (request.cookies['capp_sesion_id']):
	if "capp_sesion_id" in request.cookies:
		logeado = True
	else:
		logeado = False

	v_mostrar_categoria = mantencioncategoria.MostrarCategoria().categorias_existentes()
	v_mostrar_mediopago = mantencionmediopago.MantencionMedioPago().metodo_existente()

	v_mostrar_almuerzo = mostraralmuerzo.MostrarAlmuerzo().today_almuerzo(time.strftime("%Y-%m-%d"))

	return render_template('todo.html',ALMUERZO = v_mostrar_almuerzo, CATEGORIA = v_mostrar_categoria, logeado = logeado)

@app.route('/precio',methods = ['GET'])
def precio():
	if "capp_sesion_id" in request.cookies:
		logeado = True
	else:
		logeado = False

	v_mostrar_categoria = mantencioncategoria.MostrarCategoria().categorias_existentes()
	v_mostrar_mediopago = mantencionmediopago.MantencionMedioPago().metodo_existente()
	v_mostrar_precio = mostraralmuerzo.MostrarAlmuerzo().almuerzo_precio(time.strftime("%Y-%m-%d"))

	return render_template('precio.html', PRECIO = v_mostrar_precio, CATEGORIA = v_mostrar_categoria, MEDIO_PAGO = v_mostrar_mediopago,logeado=logeado)

@app.route('/categoria',methods=['POST'])
def categoria():
	if "capp_sesion_id" in request.cookies:
		logeado = True
	else:
		logeado = False
	v_mostrar_categoria = mantencioncategoria.MostrarCategoria().categorias_existentes()
	v_mostrar_mediopago = mantencionmediopago.MantencionMedioPago().metodo_existente()

	var = request.form.get('CAT_TYP')
	mos_almuerzo_categoria = mantencioncategoria.MostrarCategoria().search_almu_categoria(var,time.strftime("%Y-%m-%d"))
	bus_almuerzo_categoria = mantencioncategoria.MostrarCategoria().search_categorias(var)
	return render_template('categoria.html', CATEGORIA = v_mostrar_categoria,MEDIO_PAGO = v_mostrar_mediopago, CAR_NOMB = bus_almuerzo_categoria, MOSTRAR = mos_almuerzo_categoria,logeado=logeado)

@app.route('/medio_pago',methods=['POST'])
def medio_pago():
	if "capp_sesion_id" in request.cookies:
		logeado = True
	else:
		logeado = False
	v_mostrar_categoria = mantencioncategoria.MostrarCategoria().categorias_existentes()
	v_mostrar_mediopago = mantencionmediopago.MantencionMedioPago().metodo_existente()

	var = request.form.get('MT_TYP')
	bus_mediopago = mantencionmediopago.MantencionMedioPago().search_metodo(var,time.strftime("%Y-%m-%d"))

	return render_template('medio_pago.html',CATEGORIA = v_mostrar_categoria,MEDIO_PAGO = v_mostrar_mediopago, MT_NOMB = mos_mediopago, MOSTRAR = bus_mediopago,logeado=logeado)


## fin PAGINA PRINCIPAL ##

@app.route('/mas_info/<KIO_ALM_ID>',methods=['GET'])
def mas_info(KIO_ALM_ID):
	if "capp_sesion_id" in request.cookies:
		logeado = True
	else:
		logeado = False
	return render_template('masinfo.html',logeado = logeado)

@app.route('/mas_info/<KIO_ALM_ID>',methods=['POST'])
def coment_kio(KIO_ALM_ID):

	NEW = comment.Comentario()

	if NEW.create_comment(request.form["coment"],time.strftime("%Y-%m-%d"),request.form.get('T_COM'),request.form.get('VAL')):
		flash("Nuevo registro fue agregado correctamente.")
	else:
		flash("Nuevo registro no pudo ser agregado correctamente.")

	return redirect(url_for("mas_info"))



## PAGINA DE COMENTARIOS ##

@app.route('/comentar', methods=["POST"])
def comentar():
	USU_ID = request.cookies['capp_sesion_id']
	KIO_ID = request.form["KIO_ID"]
	contenido = request.form["contenido"]

	comentario = Comentario.create(USU_ID, KIO_id, contenido)
	if (comentario == "creado"):
		index
	else:
		flash("No se pudo crear")

## fin PAGINA DE COMENTARIOS ##

## PROCESO DE LOGIN ##

@app.route('/inicio', methods=["GET"]) # página de inicio de sesión del sistema
def inicio():
	return render_template('inicio.html')

@app.route('/inicio', methods=["POST"])
def procesar_inicio():
	email = request.form["USU_CORREO"]
	contrasena = request.form["USU_CONTRASENA"]

	# TODO: Buscar usuario por email y ver si contraseña es válida.
	usuario = login.LoginComeacApp().find_usuario_correo(email)

	if (usuario and usuario['USU_CONTRASENA'] == contrasena):
		valido = True
	else:
		valido = False

	if (valido):
		# Switch para ver a donde debe redirigir
		if usuario['USU_TIP_USU'] == 1:
			response = app.make_response(redirect(url_for('index')))
		elif usuario['USU_TIP_USU'] == 2:
			response = app.make_response(redirect(url_for('adminkiosco')))
		elif usuario['USU_TIP_USU'] == 3:
			response = app.make_response(redirect(url_for('ADM_kioscos')))
		else:
			response = app.make_response(redirect(url_for('admisystem')))
		response.set_cookie('capp_sesion_id', bytes(usuario['USU_ID'])) # crear la cookie
	else:
		response = app.make_response(redirect(url_for('inicio')))
		flash('No puedes iniciar sesión')

	return response

## fin PROCESO LOGING ##

## PROCESO LOGOUT ##

@app.route('/salir', methods=['GET'])
def cerrar_sesion():
	response = app.make_response(redirect(url_for('inicio')))
	response.set_cookie('capp_sesion_id', '', expires=0)
	flash('Sesión cerrada con exito.')

	return response

## fin PROCESO LOGOUT


@app.route('/adminkiosco') # página principal del administrador del kiosco [Administrador de Kiosco]
def adminkiosco():
	if "capp_sesion_id" in request.cookies:
		logeado = True
	else:
		logeado = False

	return render_template('adminkiosco.html', logeado = logeado)



@app.route('/gestreporte') # página de la gestión de reportes [Administrador de Kiosco]
def gestreporte():
	if "capp_sesion_id" in request.cookies:
		logeado = True
	else:
		logeado = False

	return render_template('gestreporte.html',logeado=logeado)







#FUNCIONES DE CONTROL DE USUARIO

#ACCESO A LA RUTA PRINCIPAL: Se muestran los usuarios.
@app.route('/regusuario', methods = ['GET'])
def regusuario():
	if "capp_sesion_id" in request.cookies:
		logeado = True
	else:
		logeado = False
	v_regusuario = registrousuario.RegistroUsuario().all_usuario()
	v_mostrar_tipousuario = mantenciontipousuario.MantencionTipoUsuario().all_tipousuario()
	v_mostrar_permiso = mantencionpermiso.MantencionPermiso().all_permiso()

	return render_template('regusuario.html', TIPO_USUARIO = v_mostrar_tipousuario, PERMISO = v_mostrar_permiso, USUARIO = v_regusuario,logeado=logeado)

#REGISTRO DE USUARIO NUEVO
@app.route('/regusuario', methods = ['POST'])
def crear_usuario():
	v_crear_usuario = registrousuario.RegistroUsuario()

	ban = request.form.get('bancheck')
	if not ban:
		ban = "0"
	else:
		ban = "1"

	if v_crear_usuario.create_usuario(request.form['USU_CORREO'], request.form['USU_NOMBRE'], request.form['USU_CONTRASENA'],request.form.get('test1'), ban) and v_crear_usuario.asign_permiso_usuario(request.form['USU_CORREO'], request.form.get('test2'), time.strftime("%Y-%m-%d")):
		flash("Nuevo registro fue agregado correctamente.")
	else:
		flash("Nuevo registro no pudo ser agregado correctamente.")

	return redirect(url_for("regusuario"))

#fin FUNCIONES DE CONTROL DE USUARIO


##FUNCIONES DE KIOSCOS##

#ACCESO A LA RUTA PRINCIPAL: Se muestran los kioscos.
@app.route("/ADM_kioscos", methods = ['GET'])
def ADM_kioscos():
	if "capp_sesion_id" in request.cookies:
		logeado = True
	else:
		logeado = False

	v_get_kiosco = registrokiosco.RegistroKiosco().all_kiosco()
	v_get_universidad = mantencionuniversidad.MantencionUniversidad().all_universidad()
	v_get_carrera = mantencioncarrera.MantencionCarrera().all_carrera()

	return render_template("gestkiosco.html", KIOSCO = v_get_kiosco, UNIVERSIDAD = v_get_universidad, CARRERA = v_get_carrera,logeado = logeado)

#REGISTRO DE KIOSCO NUEVO
@app.route("/ADM_kioscos",methods = ['POST'])
def crear_kiosco():

	v_crear_kiosco = registrokiosco.RegistroKiosco()

	if v_crear_kiosco.create_kiosco(request.form['KIO_NOMBRE'],request.form['KIO_DIRECCION'],request.form.get('KIO_CARR'),request.form.get('KIO_UNIV')):
		flash("Nuevo registro fue agregado correctamente.")
	else:
		flash("Nuevo registro no pudo ser agregado correctamente.")

	return redirect(url_for("ADM_kioscos"))

#ACTUALIZACION DE DATOS KIOSCO

@app.route("/ADM_kioscos/<KIO_ID>/UPD")
def editar_kiosco(KIO_ID):
	if "capp_sesion_id" in request.cookies:
		logeado = True
	else:
		logeado = False
	v_editar_kiosco = registrokiosco.RegistroKiosco()
	v_get_universidad = mantencionuniversidad.MantencionUniversidad().all_universidad()
	v_get_carrera = mantencioncarrera.MantencionCarrera().all_carrera()

	return render_template("edit_kiosco.html", EDITAR = v_editar_kiosco.find_kiosco(KIO_ID),UNIVERSIDAD = v_get_universidad,CARRERA = v_get_carrera,logeado=logeado)

@app.route("/ADM_kioscos/<KIO_ID>/UPD",methods = ['POST'])
def actualizar_kiosco(KIO_ID):

	v_actualizar_kiosco = registrokiosco.RegistroKiosco()

	if v_actualizar_kiosco.update_kiosco(KIO_ID,request.form['KIO_NOMBRE'],request.form['KIO_DIRECCION'],request.form.get('KIO_CARR'),request.form.get('KIO_UNIV')):
		flash("Registro fue actualizado correctamente.")
	else:
		flash("Registro no puede ser actualizado.")

	return redirect(url_for("ADM_kioscos"))

#ELIMINACION DE DATOS KIOSCO

@app.route("/ADM_kioscos/<KIO_ID>/DEL")
def eliminar_kiosco(KIO_ID):

	v_eliminar_kiosco = registrokiosco.RegistroKiosco()
	if v_eliminar_kiosco.destroy_kiosco(KIO_ID):
		flash("Registro fue eliminado correctamente.")
	else:
		flash("Registro no pudo ser eliminado.")

	return redirect(url_for("ADM_kioscos"))


#ASIGNACION DE KIOSCOS

@app.route("/ADM_kioscos/ASG_user",methods = ['GET'])
def asignar_kiosco():
	if "capp_sesion_id" in request.cookies:
		logeado = True
	else:
		logeado = False
	v_get_KioUsuario = registrousuario.RegistroUsuario().search_kioUsuario()
	v_get_admnKio = registrousuario.RegistroUsuario().search_admKiosco()
	v_get_notassigned = registrousuario.RegistroUsuario().not_assigned()
	#v_get_admKiosco = registrousuario().RegistroUsuario().search_admKiosco()
	#v_get_kiosco = registrokiosco.RegistroKiosco().all_kiosco()

	#v_get_universidad = mantencionuniversidad.MantencionUniversidad().all_universidad()
	#v_get_carrera = mantencioncarrera.MantencionCarrera().all_carrera()

	return render_template("gestadmin_kiosco.html", ADM_KIOSCO = v_get_KioUsuario, USR_KADM = v_get_admnKio, NOT_ASSIGNED = v_get_notassigned,logeado=logeado)

@app.route("/ADM_kioscos/ASG_user",methods = ['POST'])
def asignacion_kiosco():

	v_asignar_usuario = registrousuario.RegistroUsuario()

	if v_asignar_usuario.asign_kiosco_usuario(request.form.get('administradores_kio'),request.form.get('kioscos'),time.strftime("%Y-%m-%d")):
		flash("Nuevo registro fue agregado correctamente.")
	else:
		flash("Nuevo registro no pudo ser agregado correctamente.")

	return redirect(url_for("asignar_kiosco"))

##fin FUNCIONES DE KIOSCOS##



# Registro Kiosco



@app.route('/adminsystem', methods = ['GET']) # página principal del administrador del sistema [Administrador del Sistema]
def admisystem():
	if "capp_sesion_id" in request.cookies:
		logeado = True
	else:
		logeado = False
	v_mostrar_carrera = mantencioncarrera.MantencionCarrera().all_carrera()
	v_mostrar_universidad = mantencionuniversidad.MantencionUniversidad().all_universidad()
	v_mostrar_mediopago = mantencionmediopago.MantencionMedioPago().all_mediopago()
	v_mostrar_administradores = registrokiosco.RegistroKiosco().search_admin_user()


	return render_template('adminsystem.html', CARRERA = v_mostrar_carrera, UNIVERSIDAD = v_mostrar_universidad, MEDIO_PAGO = v_mostrar_mediopago, ADMIN_USER = v_mostrar_administradores,logeado=logeado)

# Fin Registro Kiosco





# Mantención de tablas básica



@app.route("/mantencion_tablasbasicas") # página de mantención de tablas básicas [Administrador del Sistema]
def mantencion_tablasbasicas():
	if "capp_sesion_id" in request.cookies:
		logeado = True
	else:
		logeado = False
	return render_template("mantencion_tablasbasicas.html",logeado=logeado)



# Mantención Medio de Pago



@app.route("/mantencion_mediopago", methods = ['GET']) # página de mantención de medio de pago
def mantencion_mediopago():
	if "capp_sesion_id" in request.cookies:
		logeado = True
	else:
		logeado = False
	v_mantencion_mediopago = mantencionmediopago.MantencionMedioPago().all_mediopago()
	return render_template("mantencion_mediopago.html", MEDIO_PAGO = v_mantencion_mediopago,logeado=logeado)



@app.route("/mantencion_mediopago", methods = ['POST']) # crea un nuevo medio de pago
def crear_mediopago():
	v_crear_mediopago = mantencionmediopago.MantencionMedioPago()
	if v_crear_mediopago.create_mediopago(request.form['MED_PAG_NOMBRE']):
		flash("Nuevo registro fue agregado correctamente.")
	else:
		flash("Nuevo registro no pudo ser agregado correctamente.")

	return redirect(url_for("mantencion_mediopago"))



@app.route("/mantencion_mediopago/<MED_PAG_ID>/delete") # elimina un medio de pago
def eliminar_mediopago(MED_PAG_ID):
	v_eliminar_mediopago = mantencionmediopago.MantencionMedioPago()
	if v_eliminar_mediopago.destroy_mediopago(MED_PAG_ID):
		flash("Registro fue eliminado correctamente.")
	else:
		flash("Registro no pudo ser eliminado.")

	return redirect(url_for("mantencion_mediopago"))



@app.route("/edit_mediopago/<MED_PAG_ID>", methods = ['GET']) # página para editar un medio de pago
def editar_mediopago(MED_PAG_ID):
	if "capp_sesion_id" in request.cookies:
		logeado = True
	else:
		logeado = False
	v_editar_mediopago = mantencionmediopago.MantencionMedioPago()
	return render_template("edit_mediopago.html", editar = v_editar_mediopago.find_mediopago(MED_PAG_ID),logeado=logeado)



@app.route("/edit_mediopago/<MED_PAG_ID>", methods = ['POST']) # registra un medio de pago actualizado
def actualizar_mediopago(MED_PAG_ID):
	v_actualizar_mediopago = mantencionmediopago.MantencionMedioPago()
	if v_actualizar_mediopago.update_mediopago(MED_PAG_ID, request.form['MED_PAG_NOMBRE']):
		flash("Registro fue actualizado correctamente.")
	else:
		flash("Registro no puede ser actualizado.")

	return redirect(url_for("mantencion_mediopago"))



# Fin Mantención Medios de Pagos



# Mantención de carrera



@app.route("/mantencion_carrera", methods = ['GET']) # mantención de la tabla CARRERA [Administrador del Sistema]
def mantencion_carrera(): # muestra todas las carreras de la base de datos
	if "capp_sesion_id" in request.cookies:
		logeado = True
	else:
		logeado = False
	v_mostrar_carrera = mantencioncarrera.MantencionCarrera().all_carrera()
	return render_template('mantencion_carrera.html', CARRERA = v_mostrar_carrera,logeado=logeado)



@app.route("/edit_carrera/<CAR_ID>", methods = ['GET']) # página para editar la carrera
def editar_carrera(CAR_ID):
	if "capp_sesion_id" in request.cookies:
		logeado = True
	else:
		logeado = False
	v_editar_carrera = mantencioncarrera.MantencionCarrera()
	return render_template('edit_carrera.html', editar = v_editar_carrera.find_carrera(CAR_ID),logeado=logeado)



@app.route("/edit_carrera/<CAR_ID>", methods = ['POST']) # registra la carrera actualizada
def actualizar_carrera(CAR_ID):
	v_actualizar_carrera = mantencioncarrera.MantencionCarrera()
	if v_actualizar_carrera.update_carrera(CAR_ID, request.form['CAR_NOMBRE']):
		flash("Registro fue actualizado correctamente.")
	else:
		flash("Registro no puede ser actualizado.")

	return redirect(url_for('mantencion_carrera'))



@app.route("/mantencion_carrera", methods = ['POST']) # crea una nueva carrera
def crear_carrera():
	v_crear_carrera = mantencioncarrera.MantencionCarrera()
	if v_crear_carrera.create_carrera(request.form['CAR_NOMBRE']):
		flash("Nuevo registro fue agregado correctamente")
	else:
		flash("Nuevo registro no pudo ser agregado correctamente")

	return redirect(url_for('mantencion_carrera'))



@app.route("/mantencion_carrera/<CAR_ID>/delete") # elimina una carrera ya creada
def eliminar_carrera(CAR_ID):
	v_eliminar_carrera = mantencioncarrera.MantencionCarrera()
	if v_eliminar_carrera.destroy_carrera(CAR_ID):
		flash("Registro fue eliminado correctamente")
	else:
		flash("Registro no puede ser eliminado")

	return redirect(url_for('mantencion_carrera'))



# Fin Mantención de carrera



# Mantención de universidad



@app.route("/mantencion_universidad", methods = ['GET']) # mantención de la tabla UNIVERSIDAD [Administrador del Sistema]
def mantencion_universidad(): # muestra todas las universidades de la base de datos
	if "capp_sesion_id" in request.cookies:
		logeado = True
	else:
		logeado = False
	v_mostrar_universidad = mantencionuniversidad.MantencionUniversidad().all_universidad()
	return render_template('mantencion_universidad.html', UNIVERSIDAD = v_mostrar_universidad,logeado=logeado)



@app.route("/edit_universidad/<UNI_ID>", methods = ['GET']) # página para editar la universidad
def editar_universidad(UNI_ID):
	if "capp_sesion_id" in request.cookies:
		logeado = True
	else:
		logeado = False
	v_editar_universidad = mantencionuniversidad.MantencionUniversidad()
	return render_template('edit_universidad.html', editar = v_editar_universidad.find_universidad(UNI_ID),logeado=logeado)



@app.route("/edit_universidad/<UNI_ID>", methods = ['POST']) # registra la universidad actualizada
def actualizar_universidad(UNI_ID):
	v_actualizar_universidad = mantencionuniversidad.MantencionUniversidad()
	if v_actualizar_universidad.update_universidad(UNI_ID, request.form['UNI_NOMBRE']):
		flash("Registro fue actualizado correctamente.")
	else:
		flash("Registro no puede ser actualizado.")

	return redirect(url_for('mantencion_universidad'))



@app.route("/mantencion_universidad", methods = ['POST']) # crea una nueva carrera
def crear_universidad():
	v_crear_universidad = mantencionuniversidad.MantencionUniversidad()
	if v_crear_universidad.create_universidad(request.form['UNI_NOMBRE']):
		flash("Nuevo registro fue agregado correctamente")
	else:
		flash("Nuevo registro no pudo ser agregado correctamente")

	return redirect(url_for('mantencion_universidad'))



@app.route("/mantencion_universidad/<UNI_ID>/delete") # elimina una carrera ya creada
def eliminar_universidad(UNI_ID):
	v_eliminar_universidad = mantencionuniversidad.MantencionUniversidad()
	if v_eliminar_universidad.destroy_universidad(UNI_ID):
		flash("Registro fue eliminado correctamente")
	else:
		flash("Registro no puede ser eliminado")

	return redirect(url_for('mantencion_universidad'))



# Fin Mantención de universidad



# Mantención de tipo de usuario



@app.route("/mantencion_tipousuario", methods = ['GET']) # mantención de la tabla TIPO_USUARIO [Administrador del Sistema]
def mantencion_tipousuario(): # muestra todos los tipos de usuario de la base de datos
	if "capp_sesion_id" in request.cookies:
		logeado = True
	else:
		logeado = False
	v_mostrar_tipousuario = mantenciontipousuario.MantencionTipoUsuario().all_tipousuario()
	return render_template('mantencion_tipousuario.html', TIPO_USUARIO = v_mostrar_tipousuario,logeado=logeado)



@app.route("/edit_tipousuario/<TIP_USU_ID>", methods = ['GET']) # página para editar los tipos de usuarios
def editar_tipousuario(TIP_USU_ID):
	if "capp_sesion_id" in request.cookies:
		logeado = True
	else:
		logeado = False
	v_editar_tipousuario = mantenciontipousuario.MantencionTipoUsuario()
	return render_template('edit_tipousuario.html', editar = v_editar_tipousuario.find_tipousuario(TIP_USU_ID),logeado=logeado)



@app.route("/edit_tipousuario/<TIP_USU_ID>", methods = ['POST']) # registra los tipos de usuarios actualizados
def actualizar_tipousuario(TIP_USU_ID):
	v_actualizar_tipousuario = mantenciontipousuario.MantencionTipoUsuario()
	if v_actualizar_tipousuario.update_tipousuario(TIP_USU_ID, request.form['TIP_USU_NOMBRE']):
		flash("Registro fue actualizado correctamente.")
	else:
		flash("Registro no puede ser actualizado.")

	return redirect(url_for('mantencion_tipousuario'))



@app.route("/mantencion_tipousuario", methods = ['POST']) # crea un nuevo tipo de usuario
def crear_tipousuario():
	v_crear_tipousuario = mantenciontipousuario.MantencionTipoUsuario()
	if v_crear_tipousuario.create_tipousuario(request.form['TIP_USU_NOMBRE']):
		flash("Nuevo registro fue agregado correctamente")
	else:
		flash("Nuevo registro no pudo ser agregado correctamente")

	return redirect(url_for('mantencion_tipousuario'))



@app.route("/mantencion_tipousuario/<TIP_USU_ID>/delete") # elimina un tipo de usuario ya creada
def eliminar_tipousuario(TIP_USU_ID):
	v_eliminar_tipousuario = mantenciontipousuario.MantencionTipoUsuario()
	if v_eliminar_tipousuario.destroy_tipousuario(TIP_USU_ID):
		flash("Registro fue eliminado correctamente")
	else:
		flash("Registro no puede ser eliminado")

	return redirect(url_for('mantencion_tipousuario'))



# Fin Mantención de tipo de usuario



# Mantención de Permiso



@app.route("/mantencion_permiso", methods = ['GET']) # mantención de la tabla PERMISO [Administrador del Sistema]
def mantencion_permiso(): # muestra todos los permisos de la base de datos
	if "capp_sesion_id" in request.cookies:
		logeado = True
	else:
		logeado = False
	v_mostrar_permiso = mantencionpermiso.MantencionPermiso().all_permiso()
	return render_template('mantencion_permiso.html', PERMISO = v_mostrar_permiso,logeado=logeado)



@app.route("/edit_permiso/<PER_ID>", methods = ['GET']) # página para editar los permiso
def editar_permiso(PER_ID):
	if "capp_sesion_id" in request.cookies:
		logeado = True
	else:
		logeado = False
	v_editar_permiso = mantencionpermiso.MantencionPermiso()
	return render_template('edit_permiso.html', editar = v_editar_permiso.find_permiso(PER_ID),logeado=logeado)



@app.route("/edit_permiso/<PER_ID>", methods = ['POST']) # registra los permisos actualizados
def actualizar_permiso(PER_ID):
	v_actualizar_permiso = mantencionpermiso.MantencionPermiso()
	if v_actualizar_permiso.update_permiso(PER_ID, request.form['PER_NOMBRE']):
		flash("Registro fue actualizado correctamente.")
	else:
		flash("Registro no puede ser actualizado.")

	return redirect(url_for('mantencion_permiso'))

@app.route("/mantencion_permiso", methods = ['POST']) # crea un nuevo tipo de usuario
def crear_permiso():
	v_crear_permiso = mantencionpermiso.MantencionPermiso()
	if v_crear_permiso.create_permiso(request.form['PER_NOMBRE']):
		flash("Nuevo registro fue agregado correctamente")
	else:
		flash("Nuevo registro no pudo ser agregado correctamente")

	return redirect(url_for('mantencion_permiso'))



@app.route("/mantencion_permiso/<PER_ID>/delete") # elimina un tipo de usuario ya creada
def eliminar_permiso(PER_ID):
	v_eliminar_permiso = mantencionpermiso.MantencionPermiso()
	if v_eliminar_permiso.destroy_permiso(PER_ID):
		flash("Registro fue eliminado correctamente")
	else:
		flash("Registro no puede ser eliminado")

	return redirect(url_for('mantencion_permiso'))



# Fin Mantención de Permiso



# Mantención Almuerzo



@app.route("/mantencion_almuerzo", methods = ['GET']) # página de mantención de medio de pago
def mantencion_almuerzo():
	if "capp_sesion_id" in request.cookies:
		logeado = True
	else:
		logeado = False
	v_mantencion_almuerzo = mantencionalmuerzo.MantencionAlmuerzo().all_almuerzo()
	return render_template("mantencion_almuerzo.html", ALMUERZO = v_mantencion_almuerzo,logeado=logeado)


@app.route("/mantencion_almuerzo", methods = ['POST']) # crea un nuevo medio de pago
def crear_almuerzo():
	v_crear_almuerzo = mantencionalmuerzo.MantencionAlmuerzo()
	if v_crear_almuerzo.create_almuerzo(request.form['ALM_NOMBRE']):
		flash("Nuevo registro fue agregado correctamente.")
	else:
		flash("Nuevo registro no pudo ser agregado correctamente.")

	return redirect(url_for("mantencion_almuerzo"))



@app.route("/mantencion_almuerzo/<ALM_ID>/delete") # elimina un medio de pago
def eliminar_almuerzo(ALM_ID):
	v_eliminar_almuerzo = mantencionalmuerzo.MantencionAlmuerzo()
	if v_eliminar_almuerzo.destroy_almuerzo(ALM_ID):
		flash("Registro fue eliminado correctamente.")
	else:
		flash("Registro no pudo ser eliminado.")

	return redirect(url_for("mantencion_almuerzo"))



@app.route("/edit_almuerzo/<ALM_ID>", methods = ['GET']) # página para editar un medio de pago
def editar_almuerzo(ALM_ID):
	if "capp_sesion_id" in request.cookies:
		logeado = True
	else:
		logeado = False
	v_editar_almuerzo = mantencionalmuerzo.MantencionAlmuerzo()
	return render_template("edit_almuerzo.html", editar = v_editar_almuerzo.find_almuerzo(ALM_ID),logeado=logeado)



@app.route("/edit_almuerzo/<ALM_ID>", methods = ['POST']) # registra un medio de pago actualizado
def actualizar_almuerzo(ALM_ID):
	v_actualizar_almuerzo = mantencionalmuerzo.MantencionAlmuerzo()
	if v_actualizar_almuerzo.update_almuerzo(ALM_ID, request.form['ALM_NOMBRE']):
		flash("Registro fue actualizado correctamente.")
	else:
		flash("Registro no puede ser actualizado.")

	return redirect(url_for("mantencion_almuerzo"))



# Fin Mantención Almuerzo


if __name__ == '__main__':
	app.run(debug = True) # se encarga de ejecutar el servidor 5000
