import requests
import pandas as pd
import matplotlib.pyplot as plt

def source(accession):
    url = f"https://www.ncbi.nlm.nih.gov/nuccore/{accession}"
    response = requests.get(url)
    # Aquí se implementa el código para extraer el nombre del organismo fuente y contar la frecuencia de cada especie
    # El resultado se guarda en source_df
    source_df = pd.DataFrame(...)  # DataFrame con los datos obtenidos
    source_df.to_csv("results/source.csv", index=False)

def sequences(accession):
    url = f"https://www.ncbi.nlm.nih.gov/nuccore/{accession}"
    response = requests.get(url)
    # Aquí se implementa el código para extraer la secuencia de ADN, realizar la traducción y separación de péptidos
    # Se calcula el peso molecular e índice de estabilidad para cada péptido
    # Se crea el jointplot con los valores de peso molecular e índice de estabilidad
    # El DataFrame con los péptidos y los gráficos se guardan en glupeptides_df y fig, respectivamente
    glupeptides_df = pd.DataFrame(...)  # DataFrame con los péptidos y sus propiedades
    fig = plt.figure(...)  # Figura del jointplot
    glupeptides_df.to_csv("results/glupeptides.csv", index=False)
    fig.savefig("results/glupeptides.png")