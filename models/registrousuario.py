#!/usr/bin/env python
# -*- coding: utf-8 -*-

from db import DatabaseManager

class RegistroUsuario(object):
	def __init__(self):
		super(RegistroUsuario, self).__init__()

	def all_usuario(self): # lista todas las carreras de la base de datos
		db = DatabaseManager()
		connection= db.get_connection()

		with connection.cursor() as cursor:
			sql = " SELECT USU_ID, USU_NOMBRE, USU_CORREO, TIP_USU_NOMBRE, USU_BANEADO, PER_NOMBRE, PER_USU_F_I, PER_USU_F_T FROM USUARIO, PERMISO_USUARIO, PERMISO, TIPO_USUARIO WHERE USUARIO.USU_ID = PERMISO_USUARIO.PER_USU_ID AND PERMISO_USUARIO.PER_USU_PER = PERMISO.PER_ID AND USUARIO.USU_TIP_USU = TIPO_USUARIO.TIP_USU_ID;"
			cursor.execute(sql)
			USUARIO = cursor.fetchall()

			db.close()

			return USUARIO



	def create_usuario(self, USU_CORREO, USU_NOMBRE, USU_CONTRASENA, USU_TIP_USU, USU_BANEADO):
		db = DatabaseManager()
		connection = db.get_connection()

		with connection.cursor() as cursor:
			sql = "INSERT INTO USUARIO (USU_CORREO, USU_NOMBRE, USU_CONTRASENA, USU_TIP_USU, USU_BANEADO) VALUES ('"+USU_CORREO+"', '"+USU_NOMBRE+"', '"+USU_CONTRASENA+"', '"+USU_TIP_USU+"', '"+USU_BANEADO+"');"
			result = cursor.execute(sql)

			connection.commit()

			if result == 1 or result == '1':
				return True
			else:
				return False

	def search_admKiosco(self):
		db = DatabaseManager()
		connection= db.get_connection()

		with connection.cursor() as cursor:
			sql = " SELECT USU_ID, USU_NOMBRE, USU_CORREO FROM USUARIO WHERE USU_TIP_USU = '2' AND USU_BANEADO = '0' GROUP BY USU_NOMBRE;"
			cursor.execute(sql)
			ADMKIOSCO = cursor.fetchall()

			db.close()

			return ADMKIOSCO

	def search_kioUsuario(self):
		db = DatabaseManager()
		connection = db.get_connection()

		with connection.cursor() as cursor:
			sql = " SELECT U.USU_NOMBRE, U.USU_CORREO, K.KIO_NOMBRE,KU.KIO_USU_F_I,KU.KIO_USU_F_T FROM KIOSCO_USUARIO AS KU, KIOSCO AS K, USUARIO AS U WHERE KU.KIO_USU_KIO = K.KIO_ID AND KU.KIO_USU_ID = U.USU_ID AND KU.KIO_USU_F_T = '0000-00-00' ORDER BY `KU`.`KIO_USU_F_I` DESC;"
			cursor.execute(sql)
			KUSUARIO = cursor.fetchall()

			db.close()

			return KUSUARIO

	def not_assigned(self):
		db = DatabaseManager()
		connection = db.get_connection()

		with connection.cursor() as cursor:
			sql = "SELECT K.KIO_ID, K.KIO_NOMBRE FROM KIOSCO as K WHERE K.KIO_ID NOT IN (SELECT K.KIO_ID FROM KIOSCO_USUARIO AS KU, KIOSCO AS K, USUARIO AS U WHERE KU.KIO_USU_KIO = K.KIO_ID AND KU.KIO_USU_ID = U.USU_ID AND KU.KIO_USU_F_T = '0000-00-00');"
			cursor.execute(sql)
			NOTASG = cursor.fetchall()

			db.close()

			return NOTASG

	def asign_kiosco_usuario(self,KIO_USU_ID, KIO_USU_KIO, KIO_USU_F_I):
		db = DatabaseManager()
		connection = db.get_connection()

		with connection.cursor() as cursor:
			sql = "INSERT INTO KIOSCO_USUARIO (KIO_USU_ID, KIO_USU_KIO, KIO_USU_F_I,KIO_USU_F_T) VALUES ( '"+KIO_USU_ID+"', '"+KIO_USU_KIO+"', '"+KIO_USU_F_I+"', '0000-00-00');"
			result = cursor.execute(sql)

			connection.commit()

			if result == 1 or result == '1':
				return True
			else:
				return False
