import utils
import read_csv
import charts
#al intentar ejecutar el codigo por medio de la consola no se ejecuta nada puesto que nunca se llama a la funcion. Se necesita tener una dualidad. al ejecutar este archivo por medio de consola se debe poder ejecutar la funcion descrita en este codigo. pero tambien se debe poder ejecutar el modulo en otro archivo sin necesariamente ejecutar el codigo dentro del modulo

  #se saca la variable del scope para poder ser llamada desde otro archivo por medio del modulo.igual la funcion puede acceder al valor.




def run():
  data = read_csv.read_csv("data.csv")
  country = input("Type country => ").capitalize()
  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    print(country)
    charts.generate_bar_chart(country['Country/Territory'],labels,values)
    charts.generate_pie_chart(country['Country/Territory'],labels,values)
  
  #se pueden traer funcione

  #print(utils.A) #se pueden traer variables


if __name__ == "__main__":
  run()
#con esta sintaxis le decimos al main.py que si es llamado desde la terminal ejecute el metodo run, pero si se ejecuta desde otro archivo no se ejecute run(). Es decir se ejecuta como script.
