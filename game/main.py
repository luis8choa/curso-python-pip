import random

#sentencia continue salta hacia la siguiente iteracion del ciclo ignorando codigo posterior a esta sentencia


#truco para identar lineas de codigo - tab

def choose_options(name):
  user_option = ""
  computer_option = ""
  options = ("piedra", "papel", "tijera") #se puede convertir en una tupla de ambito local ya que solo se usa en ese caso
  while True:
    user_option = input("piedra, papel o tijera => ")
    user_option = user_option.lower()
    if user_option not in options:
      print("Esa opcion no es valida")
    else:
      break
  computer_option = random.choice(options)  #metodo random.choice(lista o tupla) selecciona un valor aleatorio del conjunto
  print(name, " option=>", user_option)
  print("Computer option=>", computer_option)
  
  return user_option, computer_option


def check_rules(user_option, computer_option,user_wins,computer_wins):
  if user_option == computer_option:
    print("Empate!")
  
  elif user_option == "piedra":
    if (computer_option == "tijera"):
      print("piedra gana a tijera")
      user_wins += 1
    else:
      print("papel gana a piedra")
      computer_wins += 1
    
  elif user_option == "papel":
    if (computer_option == "piedra"):
      print("papel gana a piedra")
      user_wins += 1
    else:
      print("tijera gana a papel")
      computer_wins += 1
    
  elif user_option == "tijera":
    if (computer_option == "papel"):
      print("tijera gana a papel")
      user_wins += 1
    else:
      print("piedra gana a tijera")
      computer_wins += 1
    
  return user_wins, computer_wins

def winner(name,vic,user_wins,computer_wins):
  end = 0
  if user_wins == vic:
    print(name, "has ganado, felicidades!!!")
    input("Deseas Jugar otra vez?, Presiona enter para continuar")
    end = 1 
  return end
  
    
  if computer_wins == vic:
    print(name, "has perdido,mejor suerte para la proxima")
    input("Deseas Jugar otra vez?, Presiona enter para continuar")
    end = 1 
  return end

def run_game(vic,name):
  computer_wins = 0
  user_wins = 0
  rounds = 1
  end = 0
  
  while True:
    print("*" * 10)
    print("ROUND", rounds)
    print("*" * 10)
    user_option, computer_option = choose_options(name)
    user_wins, computer_wins = check_rules(user_option, computer_option,user_wins,computer_wins)
    rounds += 1
    end = winner(name,vic,user_wins,computer_wins)
    if end == 1:
      break
    
    
print("Hola, Bienvenido al juego de piedra papel o tijeras")

name = str(input("Ingrese su nombre =>"))

while True:
  vic = int(
    input(
      "Indique las rondas necesarias para ganar: \n A una ronda (1) \n El mejor de tres (2) \n El mejor de cinco (3) \n =>"
    ))
  print(vic)
  run_game(vic,name)
  
  

    
