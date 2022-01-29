from flask_app.config.mysqlconnection import connectToMySQL

class Ninja():
    def __init__(self, id, first_name, last_name, age, dojoID):
        self.id = id
        self.first_name = first_name        
        self.last_name = last_name
        self.age = age
        self.dojoID = dojoID

    @classmethod
    def creaNuevoNinja(cls, dataNinja):
        query = "INSERT INTO ninjas(first_name, last_name, age, dojo_id) VALUES(%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"        
        resultado = connectToMySQL( "dojos_ninjas" ).query_db( query, dataNinja )
        return resultado # Devuelve un ID