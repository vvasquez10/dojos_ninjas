from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.modelos.Ninja import Ninja

class Dojo():
    def __init__(self, id, nombre, created_at, updated_at):
        self.id = id
        self.nombre = nombre        
        self.created_at = created_at
        self.updated_at = updated_at

    @classmethod
    def getAllDojos(cls): #Devuelve una lista de diccionarios que contienen cada objeto dojo creado
            query = "SELECT * FROM dojos;"
            result_fromDB = connectToMySQL( "dojos_ninjas" ).query_db( query )
            listaDojos = []
            for dojo in result_fromDB:
                listaDojos.append( Dojo( dojo["id"], dojo["nombre"], dojo["created_at"], dojo["updated_at"]) )
            return listaDojos
    
    @classmethod
    def buscaNinjasByDojo(cls, dojoID): # Devuelve una lista de objetos Ninja
        dataDojo = {
            'id' : dojoID
        }
        query = "select id, first_name, last_name, age, dojo_id from ninjas where dojo_id = %(id)s;" #Devuelve una lista de ninjas del dojo        
        resultado = connectToMySQL( "dojos_ninjas" ).query_db( query, dataDojo )
        listaNinjas = []
        for ninja in resultado:
            listaNinjas.append( Ninja( ninja["id"], ninja["first_name"], ninja["last_name"], ninja["age"], ninja["dojo_id"]) )
        print("gaaa", listaNinjas)
        return listaNinjas
    
    @classmethod
    def creaNuevoDojo(cls, dojoName):
        query = "INSERT INTO dojos(nombre) VALUES(%(nombre)s);"        
        resultado = connectToMySQL( "dojos_ninjas" ).query_db( query, dojoName )
        return resultado # Devuelve un ID    
