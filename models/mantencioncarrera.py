#!/usr/bin/env python
# -*- coding: utf-8 -*-

from db import DatabaseManager

class MantencionCarrera(object):
	def __init__(self):
		super(MantencionCarrera, self).__init__()

	def all_carrera(self): # lista todas las carreras de la base de datos 
		db = DatabaseManager()
		connection= db.get_connection()

		with connection.cursor() as cursor:
			sql = "SELECT CAR_ID, CAR_NOMBRE FROM CARRERA"
			cursor.execute(sql)
			CARRERA = cursor.fetchall()
		  
			db.close()

			return CARRERA

	def create_carrera(self, CAR_NOMBRE): # crea una carrera nueva dentro de la base de datos
		db = DatabaseManager()
		connection= db.get_connection()

		with connection.cursor() as cursor:
			sql = "INSERT INTO CARRERA (CAR_NOMBRE) VALUES ('"+CAR_NOMBRE+"');"
			result = cursor.execute(sql)
			
			connection.commit()
			  
			if result == 1 or result == '1':
				return True
			else:
				return False



	def destroy_carrera(self, CAR_ID): # elimina una carrera de la base de datos
		db = DatabaseManager()
		connection = db.get_connection()

		with connection.cursor() as cursor:
			sql = "DELETE FROM CARRERA WHERE CAR_ID = "+CAR_ID+" LIMIT 1;"
			result = cursor.execute(sql)

			connection.commit()

			if result == 1 or result == '1':
				return True
			else:
				return False

	

	def update_carrera(self, CAR_ID, CAR_NOMBRE): # actualiza el nombre de una carrera
		db = DatabaseManager()
		connection = db.get_connection()

		with connection.cursor() as cursor:
			sql = "UPDATE CARRERA SET CAR_NOMBRE = '"+CAR_NOMBRE+"' WHERE CAR_ID = "+CAR_ID+";"
			result = cursor.execute(sql)

			connection.commit()

			if result == 1 or result == '1':
				return True
			else:
				return False		


	def find_carrera(self, CAR_ID): # encuentra una carrera en especifico
		db = DatabaseManager()
		connection = db.get_connection()

		with connection.cursor() as cursor:
			sql = "SELECT * FROM CARRERA WHERE CAR_ID = "+CAR_ID+";"
			result = cursor.execute(sql)
			CARRERA = cursor.fetchone()

			db.close()

			return CARRERA



