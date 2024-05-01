from read_csv import read_csv
from charts import generate_bar_chart
import re

def main():
  labels = []
  values = []
  country = input('Pais aqui => ')
  data = read_csv.read_csv('./app/data.csv')
  country_data = list(filter(lambda d: d['Country/Territory']==country.capitalize(), data))
  for key, value in country_data[0].items():
    if re.match('[0-9]{4} Population', key):
      labels.append(key.replace(' Population', ''))
      values.append(int(value))
  generate_bar_chart(labels, values)

if __name__ == '__main__':
  main()
  