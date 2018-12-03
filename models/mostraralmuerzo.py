#!/usr/bin/env python
# -*- coding: utf-8 -*-

from db import DatabaseManager

class MostrarAlmuerzo(object):
	def __init__(self):
		super(MostrarAlmuerzo, self).__init__()

	def all_almuerzo(self): # lista todas las carreras de la base de datos
		db = DatabaseManager()
		connection = db.get_connection()

		with connection.cursor() as cursor:
			sql = "SELECT K.KIO_ID, K.KIO_NOMBRE,A.ALM_NOMBRE, KA.PRECIO,KA.HORA,KA.FECHA FROM ALMUERZO as A, KIOSCO_ALMUERZO as KA, KIOSCO as K WHERE KA.KIO_ALM_ALM = A.ALM_ID AND KA.KIO_ALM_KIO = K.KIO_ID;"
			cursor.execute(sql)
			ALMUERZO = cursor.fetchall()

			db.close()

			return ALMUERZO

	def today_almuerzo(self,KIO_FECHA):
		db = DatabaseManager()
		connection = db.get_connection()

		with connection.cursor() as cursor:
			sql = "SELECT KA.KIO_ALM_ID,K.KIO_ID, K.KIO_NOMBRE,A.ALM_NOMBRE, KA.PRECIO,KA.HORA,KA.FECHA FROM ALMUERZO as A, KIOSCO_ALMUERZO as KA, KIOSCO as K WHERE KA.KIO_ALM_ALM = A.ALM_ID AND KA.KIO_ALM_KIO = K.KIO_ID AND KA.Fecha = '"+KIO_FECHA+"'  ORDER BY `A`.`ALM_NOMBRE` ASC;"
			cursor.execute(sql)
			TODAY = cursor.fetchall()

			db.close()

			return TODAY


	def almuerzo_precio(self,KIO_FECHA):
		db = DatabaseManager()
		connection = db.get_connection()

		with connection.cursor() as cursor:
			sql = "SELECT KA.KIO_ALM_ID,A.ALM_ID, A.ALM_NOMBRE,C.CAT_ID,C.CAT_NOMBRE,KA.PRECIO FROM KIOSCO_ALMUERZO as KA, ALMUERZO as A, CATEGORIA as C WHERE KA.KIO_ALM_ALM = A.ALM_ID AND KA.KIO_ALM_CAT = C.CAT_ID AND KA.Fecha = '"+KIO_FECHA+"' ORDER BY `KA`.`PRECIO` ASC ;"
			cursor.execute(sql)
			A_PRECIO = cursor.fetchall()

			db.close()

			return A_PRECIO


	def find_kiosco(self, KIO_ALM_ID): # encuentra una carrera en especifico
		db = DatabaseManager()
		connection = db.get_connection()

		with connection.cursor() as cursor:
			sql = "SELECT * FROM KIOSCO_ALMUERZO WHERE KIO_ALM_ID = "+KIO_ALM_ID+";"
			result = cursor.execute(sql)
			KIOSCO_ALMUERZO = cursor.fetchone()

			db.close()

			return KIOSCO_ALMUERZO
