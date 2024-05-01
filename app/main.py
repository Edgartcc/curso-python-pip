import utils # estamos llamando el archivo donde esta la funcion get_population y este es el modulo que hemos creado

import read_csv
import charts
# esta es la lista con diccionario:
'''
data = [
  {
    'Country': 'Colombia',
    'Population': 500
  },
  {
    'Country': 'Bolivia',
    'Population': 300
  }
]
'''
#definimos una funcion para que solo funcione si la pedimos, o sea si escribimos main.run()
def run():
  #keys, values = utils.get_population()
  #print(keys, values)
  data = read_csv.read_csv('data.csv')
  # tambien podemos filtrar la informacion para el reto 2
  # data = list(filter(lambda item : item['Continent'] == 'South America', data))
  countries = list(map(lambda x: x['Country/Territory'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(countries, percentages)

  country = input('Type Country => ')
  
  
  # le enviamos dos parametros, data, que es la lista donde esta la informacion y el segundo es el pais que deseamos obtener.
  # result = utils.population_by_country(data, 'Colombia')
  
  # pero ahora usando input, en vez de 'Colombia', ponemos country
  result = utils.population_by_country(data, country)

  if len(result) > 0: # o sea que encontro algun pais
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country/Territory'], labels, values)

  
  

# pero ahora main.py ya no sirve desde la terminal(shell) puedes usar if. Este if le dice al archivo main.py que si es ejecutado desde la terminal ejecute run, pero no desde otro archivo

if __name__ == '__main__':
  run()