#!/usr/bin/env python
# -*- coding: utf-8 -*-

from db import DatabaseManager

class MantencionTipoUsuario(object):
	def __init__(self):
		super(MantencionTipoUsuario, self).__init__()

	def all_tipousuario(self): # lista todas las carreras de la base de datos 
		db = DatabaseManager()
		connection= db.get_connection()

		with connection.cursor() as cursor:
			sql = "SELECT TIP_USU_ID, TIP_USU_NOMBRE FROM TIPO_USUARIO"
			cursor.execute(sql)
			TIPO_USUARIO = cursor.fetchall()
		  
			db.close()

			return TIPO_USUARIO

	def create_tipousuario(self, TIP_USU_NOMBRE): # crea una carrera nueva dentro de la base de datos
		db = DatabaseManager()
		connection= db.get_connection()

		with connection.cursor() as cursor:
			sql = "INSERT INTO TIPO_USUARIO (TIP_USU_NOMBRE) VALUES ('"+TIP_USU_NOMBRE+"');"
			result = cursor.execute(sql)
			
			connection.commit()
			  
			if result == 1 or result == '1':
				return True
			else:
				return False



	def destroy_tipousuario(self, TIP_USU_ID): # elimina una carrera de la base de datos
		db = DatabaseManager()
		connection = db.get_connection()

		with connection.cursor() as cursor:
			sql = "DELETE FROM TIPO_USUARIO WHERE TIP_USU_ID = "+TIP_USU_ID+" LIMIT 1;"
			result = cursor.execute(sql)

			connection.commit()

			if result == 1 or result == '1':
				return True
			else:
				return False

	

	def update_tipousuario(self, TIP_USU_ID, TIP_USU_NOMBRE): # actualiza el nombre de una carrera
		db = DatabaseManager()
		connection = db.get_connection()

		with connection.cursor() as cursor:
			sql = "UPDATE TIPO_USUARIO SET TIP_USU_NOMBRE = '"+TIP_USU_NOMBRE+"' WHERE TIP_USU_ID = "+TIP_USU_ID+";"
			result = cursor.execute(sql)

			connection.commit()

			if result == 1 or result == '1':
				return True
			else:
				return False		


	def find_tipousuario(self, TIP_USU_ID): # encuentra una carrera en especifico
		db = DatabaseManager()
		connection = db.get_connection()

		with connection.cursor() as cursor:
			sql = "SELECT * FROM TIPO_USUARIO WHERE TIP_USU_ID = "+TIP_USU_ID+";"
			result = cursor.execute(sql)
			TIPO_USUARIO = cursor.fetchone()

			db.close()

			return TIPO_USUARIO



