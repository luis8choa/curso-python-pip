import matplotlib.pyplot as plt  #alias para ser mas sencillo usar metodos


def generate_bar_chart(name,labels,values):

  fig, ax = plt.subplots()
  ax.bar(labels, values)
  #plt.show() #queda corriendo en terminal, para salir usar ctrl + c
  plt.savefig(f'./imgs/{name}_bar.png')
  plt.close()

def generate_pie_chart(name,labels,values):

  fig, ax = plt.subplots()
  ax.pie(values, labels=labels) #en pie chart, primero se mandan los valores como argumento y luego el otro argumento es indicar cuales son los labels, en este caso "labels"
  ax.axis("equal") # centrado (.axis()) y en forma de circulo "equal"
  #plt.show() #queda corriendo en terminal, para salir usar ctrl + c
  plt.savefig(f'./imgs/{name}_pie.png')
  plt.close()



if __name__ == "__main__":
  #haremos este metodo dinamico, es decir enviar valores y reutilizar funcion varias veces
  labels = ["a", "b", "c"]  # array de labels para la grafica
  values = [100, 40, 800]  #array de valores para la grafica
  generate_bar_chart(labels,values)
  generate_pie_chart(labels, values)
