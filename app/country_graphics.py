import read_csv, charts


def select_country_index(n, c_l):
  index = 0
  result = 0
  for c in c_l:
    if n == c:
      result = index
      return result
      break
    index += 1
  print("Country is invalid")


def graphic_country_pop(pop_l, c_l):
  while True:
    print("Select a country from the following list: ")
    for element in c_l:
      print(element)
    n = input("Country => ").capitalize()

    if n in c_l:
      break
    print("invalid country")
  index = select_country_index(n, c_l)
  pops = pop_l[index]
  pops.pop("Country")
  labels = list(pops.keys())
  values = list(map(lambda x: float(x), list(pops.values())))
  #print(type(labels[0]))
  #print(type(values[0]))
  #print(labels)
  #print(values)
  charts.generate_bar_chart(labels, values)


data = read_csv.read_csv("./app/data.csv")
#print(data)
new_data = []
country_list = []

for country in data:
  pop = {
    "Country": country["Country/Territory"],
    "2022": country["2022 Population"],
    "2020": country["2020 Population"],
    "2015": country["2015 Population"],
    "2010": country["2010 Population"],
    "2000": country["2000 Population"],
    "1990": country["1990 Population"],
    "1980": country["1980 Population"],
    "1970": country["1970 Population"]
  }
  new_data.append(pop)

for country in data:
  country_name = country["Country/Territory"]
  country_list.append(country_name)

graphic_country_pop(new_data, country_list)
