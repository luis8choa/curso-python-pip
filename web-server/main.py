import store
from fastapi import FastAPI #importa el objeto
from fastapi.responses import HTMLResponse

app =  FastAPI() # creamos instancias de objeto

@app.get("/") #decorador en donde indicamos la ruta desde donde pueden ingresar en la web
def get_list():
    return[1,2,3,]


@app.get("/contact", response_class=HTMLResponse) #decorador en donde indicamos la ruta desde donde pueden ingresar en la web
def get_list():
    #return {"name": "Platzi"} # diccionario para ser convertido a formato json, 
#    se debe indicar que name es una llave por medio de corchetes y no una variable
    return """ 
        <h1>Hola soy una pagina</h1>  
        <p>Soy un parrafo3</p>

""" #estructura de una pagina html

def run():
    store.get_categories()

if __name__ == "__main__":
    run()