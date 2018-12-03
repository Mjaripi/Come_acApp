#!/usr/bin/env python
# -*- coding: utf-8 -*-

from db import DatabaseManager

class MantencionMedioPago(object):
	def __init__(self):
		super(MantencionMedioPago, self).__init__()

	def all_mediopago(self): # lista todas las carreras de la base de datos
		db = DatabaseManager()
		connection= db.get_connection()

		with connection.cursor() as cursor:
			sql = "SELECT MED_PAG_ID, MED_PAG_NOMBRE FROM MEDIO_PAGO"
			cursor.execute(sql)
			MEDIO_PAGO = cursor.fetchall()

			db.close()

			return MEDIO_PAGO

	def metodo_existente(self): # crea una carrera nueva dentro de la base de datos
		db = DatabaseManager()
		connection= db.get_connection()

		with connection.cursor() as cursor:
			sql = "SELECT MP.MED_PAG_ID, MP.MED_PAG_NOMBRE FROM KIOSCO_MEDIO_PAGO as KMP, MEDIO_PAGO as MP WHERE KMP.KIO_MED_PAG_MED = MP.MED_PAG_ID GROUP BY MP.MED_PAG_ID;"
			cursor.execute(sql)
			METODO_E = cursor.fetchall()

			db.close()

			return METODO_E

	def search_metodo(self,MT_ID,KA_DATE):
		db = DatabaseManager()
		connection = db.get_connection()

		with connection.cursor() as cursor:
			sql = "SELECT KA.KIO_ALM_ID ,K.KIO_ID,K.KIO_NOMBRE, A.ALM_ID,A.ALM_NOMBRE, KA.PRECIO, KA.HORA, MP.MED_PAG_ID,MP.MED_PAG_NOMBRE FROM kiosco_medio_pago as KMP, kiosco as K, medio_pago as MP, kiosco_almuerzo as KA, almuerzo as A WHERE KMP.KIO_MED_PAG_KIO = K.KIO_ID AND KMP.KIO_MED_PAG_MED = MP.MED_PAG_ID AND KA.KIO_ALM_KIO=K.KIO_ID AND KA.KIO_ALM_ALM = A.ALM_ID AND MP.MED_PAG_ID = '"+MT_ID+"' AND KA.Fecha = '"+KA_DATE+"';"
			cursor.execute(sql)
			S_CATEGORIA = cursor.fetchall()

			db.close()

			return S_CATEGORIA

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
			sql = "SELECT MED_PAG_ID, MED_PAG_NOMBRE FROM MEDIO_PAGO WHERE MED_PAG_ID = "+MED_PAG_ID+";"
			result = cursor.execute(sql)
			MEDIO_PAGO = cursor.fetchone()

			db.close()

			return MEDIO_PAGO
