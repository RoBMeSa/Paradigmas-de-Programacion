#======================================================
# Del directorio aplicación, el subdirectorio repositorio, 
# el archivo basededatos.py : trae el pbjeto Basededatos
#======================================================
from aplicacion.repositorio.basededatos import BaseDeDatos

#======================================================
# Del directorio aplicacion, subdirectorio repositorio,
# el archivo s3.py : trae el objeto S3
#===================================================
from aplicacion.repositorio.s3 import s3

#======================================================================
# Del directorio aplicacion, el subdirectorio repositorio,
# el archivo sistemadearchivos.py : traer el objeto SistemaDeArchivos
#======================================================================
from aplicacion.repositorio.sistemadearchivos.py import SistemaDeArchivos

#========================================================
# Del directorio aplicacion, subdirectorio models,
# el archivo usuario.py : trae el objeto Usuario
#========================================================
from aplicacion.modelos.usuario import Usuario

#=========================================================================
# Del directorio aplicacion, el subdirectorio negocios,
# el archivo manejodeinscripciones.py : trae el objeto ManejoDeInscripciones
#=========================================================================
from aplicacion.negocios.manejodeinscripciones import ManejoDeInscripciones

#=====================
#  Crear el objeto usuario
#=====================
usuario = Usuario("Roberto","Jimenez",18)

#========================
# Crear el objeto S3
#========================
repositorioS3 = S3("321321321","sdf324223","MiCubeta")

#=====================================================
# Interface inscribirUsuario del objeto ManejoDeInscripciones
#=====================================================
ManejoDeInscripciones.inscribirUsuario(usuario,repositorioS3)
print("\n")

#==============================================
# Crear el objeto sistemadearchivos
#==============================================
repositorioSistemaDeArchivos = SistemaDeArchivos("/home/users")

#===========================================================
# Interface inscribirUsuario del objeto ManejoDeInscripciones
#===========================================================
ManejoDeInscripciones.inscribirUsuario(usuario,repositorioSistemaDeArchivos)
print("\n")

#========================================
# Crear el objeto basededatos
#========================================
repositorioBaseDeDatos = BaseDeDatos("Localhost","admin", "admin123")

#==================================================================
# Interface inscribirUsuario del objeto ManejoDeInscripciones
#==================================================================
ManejoDeInscripciones.inscribirUsuario(usuario,repositorioBaseDeDatos)
print("\n")


