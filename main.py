# Importamos las librerías necesarias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def cargar_datos(ruta):
    # Se importa combinando las columnas 1 y 2 (<DTYYYYMMDD>+<TIME>)
    df = pd.read_csv(ruta, index_col=False, header=None, parse_dates=[[0, 1]])
    #Se renombran las columnas
    df.columns=["date", "Open","High","Low","Close","Volume"]
    # Establecemos la columna 'date' como índice del DataFrame
    df.set_index('date', inplace=True)
    return df

def guardar_datos(df, ruta_descarga):
    # Guardamos el DataFrame en un archivo CSV
    df.to_csv(ruta_descarga, index=True,
              header=True)
def corregir_datos(df):
    #Se comprueba el numero de nulos totales
    if df.isnull().sum().sum() > 0 :
        # Reemplazamos los valores  faltantes por la media de cada columna
        df.fillna(df.mean(), inplace=True)

def explorar_datos(df):
    # Realizamos una exploración básica de los datos
    print(df.head())  # Muestra las primeras 5 filas del DataFrame

def visualizar_datos(df):
    # Visualizamos la evolución de los precios de cierre
    plt.plot(df.index,df['Close'] )
    plt.show()

def main():

    # Ruta del archivo CSV con los datos
    ruta = 'C:\\Users\\Jose\\PycharmProjects\\pythonProject\\ciencia_datos\\DAT_MT_EURUSD_M1_2000.csv'
    ruta_descarga = 'C:\\Users\\Jose\\PycharmProjects\\pythonProject\\ciencia_datos\\DAT_MT_EURUSD_M1_2000_CABECERAS.csv'

    # Cargamos los datos del archivo CSV en un DataFrame de Pandas
    df = cargar_datos(ruta)
    # Guardamos el DataFrame en el archivo CSV, sobrescribiendo el contenido existente
    guardar_datos(df, ruta_descarga)
    # Corregimos los datos sustituyendo aquellos valores nulos por la media
    corregir_datos(df)
    # Visualizamos la evolución de los precios de cierre
    visualizar_datos(df)

if __name__ == '__main__':
    main()
