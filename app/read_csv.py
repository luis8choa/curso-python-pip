import csv #integrado en python

def read_csv(path): #definir funcion con argumento de ruta
  with open(path, "r") as csvfile: #abrelo y guardalo como un archivo con el nombre csvfile
    reader = csv.reader(csvfile,delimiter=",")
    header = next(reader) #al ser iterable, manualmente iteramos la primera fila.
    data = [] #se crea array para los diccionarios por pais
    for row in reader:
      iterable = zip(header,row) #se une la cabecera con su valor en un array de tuplas
      #print(list(iterable)) #printeamos y creamos una lista de las tuplas cabecera valor.
      country_dict = {key : value for key, value in iterable} #se itera por la llave , valor dentro del iterable, se va guardando en forma clave: valor
      data.append(country_dict) # se agrega el diccionario a el array
    return data #se devuelve el data
  

if __name__ == '__main__': #se puede llamar la funcion simplemente por la terminal, como modulo sin ejecutar el codigo.
  data = read_csv("./app/data.csv")
  #en caso de ser llamado, se guarda data
  print(data[0])



