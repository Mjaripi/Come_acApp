#!/usr/bin/env python
# -*- coding: utf-8 -*-

from db import DatabaseManager

class MostrarCategoria(object):
	def __init__(self):
		super(MostrarCategoria, self).__init__()


	def all_categoria(self):
		db = DatabaseManager()
		connection = db.get_connection()

		with connection.cursor() as cursor:
			sql = "SELECT CAT_ID,CAT_NOMBRE FROM CATEGORIA;"
			cursor.execute(sql)
			CATEGORIA = cursor.fetchall()

			db.close()

			return CATEGORIA

	def search_categorias(self,CAT_ID):
		db = DatabaseManager()
		connection = db.get_connection()

		with connection.cursor() as cursor:
			sql = "SELECT CAT_NOMBRE FROM CATEGORIA WHERE CAT_ID = '"+CAT_ID+"';"
			cursor.execute(sql)
			S_CATEGORIA = cursor.fetchall()

			db.close()

			return S_CATEGORIA

	def categorias_existentes(self):
		db = DatabaseManager()
		connection = db.get_connection()

		with connection.cursor() as cursor:
			sql = "SELECT C.CAT_ID, C.CAT_NOMBRE FROM KIOSCO_ALMUERZO as KA, CATEGORIA as C WHERE KA.KIO_ALM_CAT = C.CAT_ID GROUP BY C.CAT_ID ;"
			cursor.execute(sql)
			CATEGORIA_E = cursor.fetchall()

			db.close()

			return CATEGORIA_E


	def search_almu_categoria(self,KA_CATEGORIA,KA_DATE):
		db = DatabaseManager()
		connection = db.get_connection()

		with connection.cursor() as cursor:
			sql = "SELECT KA.KIO_ALM_ID,K.KIO_ID,K.KIO_NOMBRE,A.ALM_ID,A.ALM_NOMBRE,C.CAT_ID,C.CAT_NOMBRE, KA.PRECIO, KA.HORA FROM KIOSCO_ALMUERZO as KA, CATEGORIA as C, KIOSCO as K, ALMUERZO as A WHERE KA.KIO_ALM_CAT = C.CAT_ID AND KA.KIO_ALM_KIO = K.KIO_ID AND KA.KIO_ALM_ALM = A.ALM_ID AND C.CAT_ID = '"+KA_CATEGORIA+"'  AND KA.Fecha = '"+KA_DATE+"';"
			cursor.execute(sql)
			KA_CAT = cursor.fetchall()

			db.close()

			return KA_CAT
