#!/usr/bin/env python
# -*- coding: utf-8 -*-

from db import DatabaseManager

class RegistroKiosco(object):
	def __init__(self):
		super(RegistroKiosco, self).__init__()

	#CONSULTA QUE MUESTRA LOS KIOSCOS QUE NO HAN FIJADO HORARIO DE APERTURA Y CERRADO.

	#SELECT K.KIO_NOMBRE,C.CAR_NOMBRE, U.UNI_NOMBRE, K.KIO_UBICACION, K.KIO_APERTURA, K.KIO_CERRAR
	#FROM KIOSCO as K, CARRERA as C, UNIVERSIDAD as U
	#WHERE K.KIO_CAR_ID = C.CAR_ID AND K.KIO_UNI_ID = U.UNI_ID
	#GROUP BY K.KIO_NOMBRE
	#HAVING K.KIO_APERTURA != '00:00' AND K.KIO_CERRAR != "00:00"
	def all_kiosco(self): # lista todas las carreras de la base de datos

		db = DatabaseManager()
		connection= db.get_connection()

		with connection.cursor() as cursor:
			sql = "SELECT  K.KIO_ID,K.KIO_NOMBRE,C.CAR_NOMBRE, U.UNI_NOMBRE, K.KIO_UBICACION, K.KIO_APERTURA, K.KIO_CERRAR FROM KIOSCO as K, CARRERA as C, UNIVERSIDAD as U WHERE K.KIO_CAR_ID = C.CAR_ID AND K.KIO_UNI_ID = U.UNI_ID;"
			cursor.execute(sql)
			KIOSCO = cursor.fetchall()

			db.close()
			return KIOSCO



	def create_kiosco(self, KIO_NOMBRE, KIO_DIRECCION, KIO_CARRERA, KIO_UNIVERSIDAD):
		db = DatabaseManager()
		connection = db.get_connection()

		with connection.cursor() as cursor:
			sql = "INSERT INTO KIOSCO (KIO_NOMBRE,KIO_CAR_ID,KIO_APERTURA, KIO_UNI_ID,KIO_CERRAR,KIO_UBICACION) VALUES ('"+KIO_NOMBRE+"','"+KIO_CARRERA+"','00:00','"+KIO_UNIVERSIDAD+"','00:00','"+KIO_DIRECCION+"');"
			result = cursor.execute(sql)

			connection.commit()

			if result == 1 or result == '1':
				return True
			else:
				return False

	def update_kiosco(self,KIO_ID, KIO_NOMBRE, KIO_DIRECCION, KIO_CARRERA, KIO_UNIVERSIDAD): # actualiza el nombre de una carrera
		db = DatabaseManager()
		connection = db.get_connection()

		with connection.cursor() as cursor:
			sql = "UPDATE KIOSCO SET KIO_NOMBRE = '"+KIO_NOMBRE+"', KIO_CAR_ID = '"+KIO_CARRERA+"', KIO_UNI_ID = '"+KIO_UNIVERSIDAD+"', KIO_UBICACION = '"+KIO_DIRECCION+"' WHERE KIO_ID = "+KIO_ID+";"
			result = cursor.execute(sql)

			connection.commit()

			if result == 1 or result == '1':
				return True
			else:
				return False

	def find_kiosco(self, KIO_ID):
		db = DatabaseManager()
		connection = db.get_connection()

		with connection.cursor() as cursor:
			sql = "SELECT K.KIO_ID,K.KIO_NOMBRE,K.KIO_CAR_ID,C.CAR_NOMBRE,K.KIO_UNI_ID,U.UNI_NOMBRE,K.KIO_UBICACION FROM KIOSCO as K, UNIVERSIDAD AS U, CARRERA as C WHERE K.KIO_UNI_ID = U.UNI_ID AND K.KIO_CAR_ID = C.CAR_ID AND K.KIO_ID = '"+KIO_ID+"' "
			result = cursor.execute(sql)
			KIOSCO = cursor.fetchone()

			db.close()

			return KIOSCO

	def destroy_kiosco(self, KIO_ID):
		db = DatabaseManager()
		connection = db.get_connection()

		with connection.cursor() as cursor:
			sql = "DELETE FROM KIOSCO WHERE KIO_ID = "+KIO_ID+" LIMIT 1;"
			result = cursor.execute(sql)

			connection.commit()

			if result == 1 or result == '1':
				return True
			else:
				return False

	def asign_medio_pago(self,PER_USU_ID, PER_USU_PER, PER_USU_F_I, PER_USU_F_T):
		db = DatabaseManager()
		connection = db.get_connection()

		with connection.cursor() as cursor:
			sql = "INSERT INTO PERMISO_USUARIO (PER_USU_ID, PER_USU_PER, PER_USU_F_I, PER_USU_F_T) VALUES ('"+PER_USU_ID+"', '"+PER_USU_PER+"', '"+PER_USU_F_I+"', '"+PER_USU_F_T+"');"
			result = cursor.execute(sql)

			connection.commit()

			if result == 1 or result == '1':
				return True
			else:
				return False

	def search_admin_user(self):
		db = DatabaseManager()
		connection = db.get_connection()

		with connection.cursor() as cursor:
			sql = "SELECT USUARIO.USU_NOMBRE FROM USUARIO WHERE USUARIO.USU_TIP_USU = 3;"
			cursor.execute(sql)
			ADMIN = cursor.fetchall()

			db.close()

			return ADMIN
