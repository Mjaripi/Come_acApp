#!/usr/bin/env python
# -*- coding: utf-8 -*-

from db import DatabaseManager

class LoginComeacApp(object):
	def __init__(self):
		super(LoginComeacApp, self).__init__()


	def find_usuario(self, USU_ID): # encuentra una usuario en especifico
		db = DatabaseManager()
		connection = db.get_connection()

		with connection.cursor() as cursor:
			sql = "SELECT * FROM USUARIO WHERE USU_ID = "+USU_ID+" LIMIT 1;"
			result = cursor.execute(sql)
			USUARIO = cursor.fetchone()

			db.close()

			return USUARIO



	def find_usuario_correo(self, USU_CORREO): # encuentra una correo en especifico
		db = DatabaseManager()
		connection = db.get_connection()

		with connection.cursor() as cursor:
			sql = "SELECT * FROM USUARIO WHERE USU_CORREO = '"+USU_CORREO+"' LIMIT 1;"
			result = cursor.execute(sql)
			USUARIO = cursor.fetchone()

			db.close()

			return USUARIO
