#!/usr/bin/env python
# -*- coding: utf-8 -*-

from db import DatabaseManager

class MantencionUniversidad(object):
	def __init__(self):
		super(MantencionUniversidad, self).__init__()

	def all_universidad(self): # lista todas las carreras de la base de datos 
		db = DatabaseManager()
		connection= db.get_connection()

		with connection.cursor() as cursor:
			sql = "SELECT UNI_ID, UNI_NOMBRE FROM UNIVERSIDAD"
			cursor.execute(sql)
			UNIVERSIDAD = cursor.fetchall()
		  
			db.close()

			return UNIVERSIDAD

	def create_universidad(self, UNI_NOMBRE): # crea una carrera nueva dentro de la base de datos
		db = DatabaseManager()
		connection= db.get_connection()

		with connection.cursor() as cursor:
			sql = "INSERT INTO UNIVERSIDAD (UNI_NOMBRE) VALUES ('"+UNI_NOMBRE+"');"
			result = cursor.execute(sql)
			
			connection.commit()
			  
			if result == 1 or result == '1':
				return True
			else:
				return False



	def destroy_universidad(self, UNI_ID): # elimina una carrera de la base de datos
		db = DatabaseManager()
		connection = db.get_connection()

		with connection.cursor() as cursor:
			sql = "DELETE FROM UNIVERSIDAD WHERE UNI_ID = "+UNI_ID+" LIMIT 1;"
			result = cursor.execute(sql)

			connection.commit()

			if result == 1 or result == '1':
				return True
			else:
				return False

	

	def update_universidad(self, UNI_ID, UNI_NOMBRE): # actualiza el nombre de una carrera
		db = DatabaseManager()
		connection = db.get_connection()

		with connection.cursor() as cursor:
			sql = "UPDATE UNIVERSIDAD SET UNI_NOMBRE = '"+UNI_NOMBRE+"' WHERE UNI_ID = "+UNI_ID+";"
			result = cursor.execute(sql)

			connection.commit()

			if result == 1 or result == '1':
				return True
			else:
				return False		


	def find_universidad(self, UNI_ID): # encuentra una carrera en especifico
		db = DatabaseManager()
		connection = db.get_connection()

		with connection.cursor() as cursor:
			sql = "SELECT * FROM UNIVERSIDAD WHERE UNI_ID = "+UNI_ID+";"
			result = cursor.execute(sql)
			UNIVERSIDAD = cursor.fetchone()

			db.close()

			return UNIVERSIDAD



