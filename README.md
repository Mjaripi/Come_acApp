# Come_acApp

Para poder ejecutar Come acApp se deben seguir los siguientes pasos que poder ejecutar y compilar el sistema desarrollado en lenguaje Python en su máquina local para fines de desarrollo y pruebas. Vale mencionar que el desarrollo se llevó a cabo en un sistema Unix.
Para comenzar con la implementación necesitamos ciertos requisitos previos como Python 2, Flask 0.12.2, PyMysql, Mysql 5.6, Xampp 3.2.2, Bootstrap, Atom, DataGrip 2017.2.2 y pip (packet manager)
Instalaciones:
En el sistema Unix Python 2 viene instalado por defecto. 
Para poder instalar Flask se necesita tener previamente instalado el paquete pip, y los pasos son los siguientes:
Situado en la terminal del sistema, escribir los siguientes comandos.
1.	pip install Flask.
2.	pip install PyMySQL.

La instalación de MySQL varía según el sistema operativo utilizado, Para Mac:
1.	Ingresar al link: https://dev.mysql.com/downloads/
2.	Seleccionar MySQL Community Server.
3.	Luego hacer clic en el botón Download.
Para Ubuntu:
1.	Ingresar a terminal e ingresar los siguientes commandos.
2.	sudo apt-get update.
3.	sudo apt-get install mysql-server.
4.	mysql secure installation.
La instalación de Xampp se lleva a cabo de la siguiente forma:
1.	Ingresar al link: https://www.apachefriends.org/download.html desde el navegador web preferido.
2.	Seleccionar el Sistema Operativo.
3.	Hacer clic en el botón Download.
Para Bootstrap se necesita:
1.	Ingresar al link: https://getbootstrap.com/docs/4.0/getting-started/introduction/ desde el navegador web preferido.
2.	Copiar el link del estilo CSS, y los script de JavaScript.





Programas opcionales:
Preferencia de los programadores, no es necesaria su instalación si se utiliza otros programas que cumplen con la misma función.
Atom:
1.	Ingresar al link: https://atom.io/ desde el navegador web preferido.
2.	Hacer click en el botón Download.
DataGrip:
1.	Ingresar al link: https://www.jetbrains.com/datagrip/ desde el navegador web preferido.
2.	Hacer click en el botón Download.
Antes de compilar el sistema se debe ejecutar el script de la base de datos.
Para la compilación de Come acApp se deben seguir los siguientes pasos:
1.	Abrir la terminal del sistema
2.	Situarse en la carpeta del sistema
3.	Escribir el comando: python app.py
4.	Abrir un navegador a elección, con la url: localhost:5000
