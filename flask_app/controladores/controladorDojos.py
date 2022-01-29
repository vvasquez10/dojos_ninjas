from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.modelos.Dojo import Dojo
from flask_app.modelos.Ninja import Ninja

@app.route( '/', methods=['GET'] )
def despliegaDojos():
    dojos= Dojo.getAllDojos()
    return render_template( "dojos.html", dojos=dojos)

@app.route( '/showDojo/<int:id>/<nombre>', methods=['GET'] )
def muestraDojo(id, nombre):   # Muestra todos los integrantes del dojo a través de la func buscaNinjasByDojo()
    miDojo = Dojo.buscaNinjasByDojo(id) #Captura la lista de ninjas del dojo buscado
    #dojoName=nombre
    #print(dojoName)
    return render_template("show_dojo.html", dojo=miDojo, dojoName=nombre)

@app.route( '/createDojo', methods=['POST'] )
def creaDojo():
    nuevoDojo = {
        "nombre" : request.form["dojoName"],               
    }    
    Dojo.creaNuevoDojo( nuevoDojo )
    return redirect("/")

@app.route( '/newNinja', methods=['GET'] )
def nuevoNinja():    
    dojos = Dojo.getAllDojos()
    print (dojos[0].nombre)
    return render_template("new_ninja.html", dojos=dojos)

@app.route( '/createNinja', methods=['POST'] )
def creaNinja():
    nuevoNinja = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "age" : request.form["age"],
        "dojo_id" : request.form["dojo_id"]       ##########################        
    }    
    Ninja.creaNuevoNinja( nuevoNinja )
    return redirect("/")
