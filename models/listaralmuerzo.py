#!/usr/bin/env python
# -*- coding: utf-8 -*-

from db import DatabaseManager

class ListarAlmuerzo(object):
	def __init__(self):
		super(ListarAlmuerzo, self).__init__()

	def all_mediopago(self): # lista todas las carreras de la base de datos 
		db = DatabaseManager()
		connection= db.get_connection()

		with connection.cursor() as cursor:
			sql = "SELECT MED_PAG_ID, MED_PAG_NOMBRE FROM MEDIO_PAGO"
			cursor.execute(sql)
			MEDIO_PAGO = cursor.fetchall()
		  
			db.close()

			return MEDIO_PAGO

	def create_mediopago(self, MED_PAG_NOMBRE): # crea una carrera nueva dentro de la base de datos
		db = DatabaseManager()
		connection= db.get_connection()

		with connection.cursor() as cursor:
			sql = "INSERT INTO MEDIO_PAGO (MED_PAG_NOMBRE) VALUES ('"+MED_PAG_NOMBRE+"');"
			result = cursor.execute(sql)
			
			connection.commit()
			  
			if result == 1 or result == '1':
				return True
			else:
				return False



	def destroy_mediopago(self, MED_PAG_ID): # elimina una carrera de la base de datos
		db = DatabaseManager()
		connection = db.get_connection()

		with connection.cursor() as cursor:
			sql = "DELETE FROM MEDIO_PAGO WHERE MED_PAG_ID = "+MED_PAG_ID+" LIMIT 1;"
			result = cursor.execute(sql)

			connection.commit()

			if result == 1 or result == '1':
				return True
			else:
				return False

	

	def update_mediopago(self, MED_PAG_ID, MED_PAG_NOMBRE): # actualiza el nombre de una carrera
		db = DatabaseManager()
		connection = db.get_connection()

		with connection.cursor() as cursor:
			sql = "UPDATE MEDIO_PAGO SET MED_PAG_NOMBRE = '"+MED_PAG_NOMBRE+"' WHERE MED_PAG_ID = "+MED_PAG_ID+";"
			result = cursor.execute(sql)

			connection.commit()

			if result == 1 or result == '1':
				return True
			else:
				return False		


	def find_mediopago(self, MED_PAG_ID): # encuentra una carrera en especifico
		db = DatabaseManager()
		connection = db.get_connection()

		with connection.cursor() as cursor:
			sql = "SELECT * FROM MEDIO_PAGO WHERE MED_PAG_ID = "+MED_PAG_ID+";"
			result = cursor.execute(sql)
			MEDIO_PAGO = cursor.fetchone()

			db.close()

			return MEDIO_PAGO



