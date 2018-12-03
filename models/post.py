from db import DatabaseManager

class Post(object):
  def __init__(self):
    super(Post, self).__init__()

  def all(self):
    db = DatabaseManager()
    connection= db.get_connection()

    with connection.cursor() as cursor:
      sql = "SELECT MED_PAG_ID, MED_PAG_NOMBRE FROM MEDIO_PAGO"
      cursor.execute(sql)
      MEDIO_PAGO = cursor.fetchall()
      
      db.close()

      return MEDIO_PAGO

  def allcarrera(self):
    db = DatabaseManager()
    connection= db.get_connection()

    with connection.cursor() as cursor:
      sql = "SELECT CAR_ID, CAR_NOMBRE FROM CARRERA"
      cursor.execute(sql)
      CARRERA = cursor.fetchall()
      
      db.close()

      return CARRERA

  def alluniversidad(self):
    db = DatabaseManager()
    connection = db.get_connection()

    with connection.cursor() as cursor:
      sql = "SELECT UNI_ID, UNI_NOMBRE FROM UNIVERSIDAD"
      cursor.execute(sql)
      UNIVERSIDAD = cursor.fetchall()

      db.close()

      return UNIVERSIDAD




  def create(self, MED_PAG_NOMBRE):
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

  def create_carrera(self, CAR_NOMBRE):
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



  def destroy(self, MED_PAG_ID):
    db = DatabaseManager()
    connection= db.get_connection()

    with connection.cursor() as cursor:
      sql = "DELETE FROM MEDIO_PAGO WHERE MED_PAG_ID = "+MED_PAG_ID+" LIMIT 1;"
      result = cursor.execute(sql)
      
      connection.commit()
      
      if result == 1 or result == '1':
        return True
      else:
        return False

  def update(self, MED_PAG_ID, MED_PAG_NOMBRE):
    db = DatabaseManager()
    connection = db.get_connection()

    with connection.cursor() as cursor:
      sql = "UPDATE MEDIO_PAGO SET MED_PAG_NOMBRE = '"+MED_PAG_NOMBRE+"' WHERE MED_PAG_ID = "+MED_PAG_ID+";"
      result = cursor.execute(sql)

      connection.commit()

      if result == 1 or result =='1':
        return True
      else:
        return False

  def find(self, MED_PAG_ID):
    db = DatabaseManager()
    connection = db.get_connection()

    with connection.cursor() as cursor:
      sql = "SELECT * FROM MEDIO_PAGO WHERE MED_PAG_ID = "+MED_PAG_ID+";"
      result = cursor.execute(sql)
      med_pag = cursor.fetchone()

      db.close()

      return med_pag


