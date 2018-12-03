#!/usr/bin/env python
# -*- coding: utf-8 -*-

from db import DatabaseManager

class MantencionAlmuerzo(object):
	def __init__(self):
		super(MantencionAlmuerzo, self).__init__()

	def all_almuerzo(self): # lista todas las carreras de la base de datos 
		db = DatabaseManager()
		connection= db.get_connection()

		with connection.cursor() as cursor:
			sql = "SELECT ALM_ID, ALM_NOMBRE FROM ALMUERZO"
			cursor.execute(sql)
			ALMUERZO = cursor.fetchall()
		  
			db.close()

			return ALMUERZO

	def create_almuerzo(self, ALM_NOMBRE): # crea una carrera nueva dentro de la base de datos
		db = DatabaseManager()
		connection= db.get_connection()

		with connection.cursor() as cursor:
			sql = "INSERT INTO ALMUERZO (ALM_NOMBRE) VALUES ('"+ALM_NOMBRE+"');"
			result = cursor.execute(sql)
			
			connection.commit()
			  
			if result == 1 or result == '1':
				return True
			else:
				return False



	def destroy_almuerzo(self, ALM_ID): # elimina una carrera de la base de datos
		db = DatabaseManager()
		connection = db.get_connection()

		with connection.cursor() as cursor:
			sql = "DELETE FROM ALMUERZO WHERE ALM_ID = "+ALM_ID+" LIMIT 1;"
			result = cursor.execute(sql)

			connection.commit()

			if result == 1 or result == '1':
				return True
			else:
				return False

	

	def update_almuerzo(self, ALM_ID, ALM_NOMBRE): # actualiza el nombre de una carrera
		db = DatabaseManager()
		connection = db.get_connection()

		with connection.cursor() as cursor:
			sql = "UPDATE ALMUERZO SET ALM_NOMBRE = '"+ALM_NOMBRE+"' WHERE ALM_ID = "+ALM_ID+";"
			result = cursor.execute(sql)

			connection.commit()

			if result == 1 or result == '1':
				return True
			else:
				return False		


	def find_almuerzo(self, ALM_ID): # encuentra una carrera en especifico
		db = DatabaseManager()
		connection = db.get_connection()

		with connection.cursor() as cursor:
			sql = "SELECT * FROM ALMUERZO WHERE ALM_ID = "+ALM_ID+";"
			result = cursor.execute(sql)
			ALMUERZO = cursor.fetchone()

			db.close()

			return ALMUERZO



