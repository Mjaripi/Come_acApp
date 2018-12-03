#!/usr/bin/env python
# -*- coding: utf-8 -*-

from db import DatabaseManager

class MantencionPermiso(object):
	def __init__(self):
		super(MantencionPermiso, self).__init__()

	def all_permiso(self): # lista todas las carreras de la base de datos 
		db = DatabaseManager()
		connection= db.get_connection()

		with connection.cursor() as cursor:
			sql = "SELECT PER_ID, PER_NOMBRE FROM PERMISO"
			cursor.execute(sql)
			PERMISO = cursor.fetchall()
		  
			db.close()

			return PERMISO

	def create_permiso(self, PER_NOMBRE): # crea una carrera nueva dentro de la base de datos
		db = DatabaseManager()
		connection= db.get_connection()

		with connection.cursor() as cursor:
			sql = "INSERT INTO PERMISO (PER_NOMBRE) VALUES ('"+PER_NOMBRE+"');"
			result = cursor.execute(sql)
			
			connection.commit()
			  
			if result == 1 or result == '1':
				return True
			else:
				return False



	def destroy_permiso(self, PER_ID): # elimina una carrera de la base de datos
		db = DatabaseManager()
		connection = db.get_connection()

		with connection.cursor() as cursor:
			sql = "DELETE FROM PERMISO WHERE PER_ID = "+PER_ID+" LIMIT 1;"
			result = cursor.execute(sql)

			connection.commit()

			if result == 1 or result == '1':
				return True
			else:
				return False

	

	def update_permiso(self, PER_ID, PER_NOMBRE): # actualiza el nombre de una carrera
		db = DatabaseManager()
		connection = db.get_connection()

		with connection.cursor() as cursor:
			sql = "UPDATE PERMISO SET PER_NOMBRE = '"+PER_NOMBRE+"' WHERE PER_ID = "+PER_ID+";"
			result = cursor.execute(sql)

			connection.commit()

			if result == 1 or result == '1':
				return True
			else:
				return False		


	def find_permiso(self, PER_ID): # encuentra una carrera en especifico
		db = DatabaseManager()
		connection = db.get_connection()

		with connection.cursor() as cursor:
			sql = "SELECT * FROM PERMISO WHERE PER_ID = "+PER_ID+";"
			result = cursor.execute(sql)
			PERMISO = cursor.fetchone()

			db.close()

			return PERMISO



