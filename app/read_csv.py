# LEER UN CSV (EXCEL)

import csv

def read_csv(path): # path es la ubicacion del archivo
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')# delimiter es la forma como vienen separados los datos. El reader es iterable entonces vamos a obtener el titulo de las columnas
    header = next(reader) # esto es iterar, sacar la informacion linea por linea
    # print(header)
    data = []
    for row in reader: #  para leer fila por fila
      iterable = zip(header, row) # zip: une el header y el row en forma de tupla, los pares.
      #print(list(iterable))
      country_dict = {key: value for key, value in iterable} # asi creamos el diccionario. Ahora, vamos a poner el diccionario en una lista llamada data.
      data.append(country_dict) # lista de diccionarios con clave valor.
      # print(country_dict)
      #print('***' * 5)
      #print(row)
    return data
      #result = utils.population_by_country(data, 'Colombia')
  
    
  
  #print(result)

if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  print(data[0])
  # y asi nos queda en formato de diccionario
# queremos que quede como diccionario y no como un array de datos (desorganizados)