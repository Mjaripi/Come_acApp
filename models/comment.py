#!/usr/bin/env python
# -*- coding: utf-8 -*-

from db import DatabaseManager

class Comentario(object):
	def __init__(self):
		super(Comentario, self).__init__()

	def create_comment(self, COMENTARIO,TIME,TIPO_COM,ESTRELLAS):
		db = DatabaseManager()
		connection = db.get_connection()

		with connection.cursor() as cursor:
			sql = "INSERT INTO kiosco_comentario (KIO_COM_TIP,KIO_COM_USU,KIO_FECHA,KIO_COMENTARIO ,KIO_COM_EST,KIO_COM_ESTRELLAS,KIO_COM_KIO,KIO_COM_RECHAZO ) VALUES ('"+TIPO_COM+"','10','"+TIME+"','"+COMENTARIO+"','2','"+ESTRELLAS+"','11','');"
			result = cursor.execute(sql)

			connection.commit()

			if result == 1 or result == '1':
				return True
			else:
				return False
