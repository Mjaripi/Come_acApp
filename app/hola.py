import os
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

import sys
sys.path.insert(0, './models')
import post


app = Flask(__name__)#nuevo objeto

app.config['SECRET_KEY'] = '14e69cd065664ebcbb273a07c8105b2e338717fc4786de2479daa8b60d11e3ee9ebf16b80cd04a0ca746164fea8047be6cd76f19ede2ecb75e3ab290beacd472'


@app.route('/')#wrap o un decorador
def index():
	return render_template('index.html')

@app.route('/login')
def login():
	return 'Login'

#@app.route("/posts", methods=['GET'])
#def posts():
 # posts = Post().all()
 # return render_template('posts.html', posts=posts)

@app.route('/prueba')
def prueba():
	return render_template('prueba.html')

@app.route('/inicio')
def inicio():
	return render_template('inicio.html')


@app.route('/adminkiosco')
def adminalmuerzo():
	return render_template('adminkiosco.html')

@app.route('/gestreporte')
def gestreporte():
	return render_template('gestreporte.html')


@app.route('/adminsystem')
def admisystem():
	return render_template('adminsystem.html')


@app.route('/regusuario')
def regusuario():
	return render_template('regusuario.html')

@app.route('/mantencion', methods=['GET'])
def mantencion():
	v_posts= post.Post().all()
	return render_template('mantencion.html', MEDIO_PAGO = v_posts)

@app.route('/mantencion_carrera', methods=['GET'])
def mantencion_carrera():
	v_posts= post.Post().allcarrera()
	return render_template('mantencion_carrera.html', CARRERA = v_posts)

@app.route("/mantencion_carrera", methods=['POST'])
def create_carrera():
  v_post = post.Post()
  if v_post.create_carrera(request.form['CAR_NOMBRE']):
    flash("Nuevo registro fue agregado correctamente")
  else:
    flash("Nuevo registro no pudo ser agregado correctamente")

  return redirect(url_for('mantencion_carrera'))



@app.route("/mantencion", methods=['POST'])
def create_post():
  v_post = post.Post()
  if v_post.create(request.form['MED_PAG_NOMBRE']):
    flash("Nuevo registro fue agregado correctamente")
  else:
    flash("Nuevo registro no pudo ser agregado correctamente")

  return redirect(url_for('mantencion'))



@app.route("/mantencion/<MED_PAG_ID>/delete")
def delete_post(MED_PAG_ID):
  v_post = post.Post()
  if v_post.destroy(MED_PAG_ID):
    flash("Registro fue eliminado correctamente")
  else:
    flash("Registro no puede ser eliminado")

  return redirect(url_for('mantencion'))

@app.route("/edit", methods=['GET'])
def edit():
  v_post = post.Post()
  return render_template('edit.html', post=v_post.find(MED_PAG_ID))

@app.route("/edit/<MED_PAG_ID>/update", methods=['POST'])
def update(MED_PAG_ID):
  v_post = post.Post()
  if v_post.update(MED_PAG_ID, request.form['MED_PAG_NOMBRE']):
    flash("Post was successfully updated.")
  else:
    flash("Post can't be updated.")

  return redirect(url_for('mantencion'))




#-------------------------------

#@app.route("/posts", methods=['GET'])
#def posts():
#  posts = Post().all()
""" return render_template('posts.html', posts=posts)

@app.route("/posts", methods=['POST'])
def create_post():
	post = Post()
	if post.create(request.form['MED_PAG_NOMBRE']):
		flash("New post was successfully published")
	else:
		flash("New post can't be published")

	return redirect(url_for('posts'))

@app.route("/posts/<MED_PAG_ID>/delete")
def delete_post(MED_PAG_ID):
	post = Post()
	if post.destroy(MED_PAG_ID):
		flash("Post was successfully deleted")
	else:
		flash("Post can't be deleted")

	return redirect(url_for('posts'))

"""

if __name__ == '__main__':
	app.run(debug = True) # se encarga de ejecutar el servidor 5000