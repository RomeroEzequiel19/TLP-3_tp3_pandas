# Se importa la librería pandas y se le asigna un alias
import pandas as pd

# Se crea la función para calcular frecuencia y probabilidades
def analisis_estadistico(edades):
    
    # Se crea un DataFrame con las edades sin repetir y ordenadas de menor a mayor
    data_frame = pd.DataFrame(sorted(set(edades)), columns=['Edades'])
    # Se calcula la frecuencia absoluta de cada valor en la columna 'Edades' del DataFrame y lo almacena en la columna 'fi'.
    data_frame['fi'] = [edades.count(valor) for valor in data_frame['Edades']]
    # Se calcula la frecuencia acumulada (Fi)
    data_frame["Fi"] = data_frame['fi'].cumsum()
    # Se calcula la frecuancia relativa (ri)
    data_frame["ri"] = data_frame["fi"] / data_frame["fi"].sum()
    # Se calcula la frecuencia relativa acumulada (Ri)
    data_frame["Ri"] = data_frame["ri"].cumsum()
    # Se calcula la probabilidad (pi)
    data_frame["pi"] = data_frame["ri"] * 100
    # Se calcula la probabilidad acumulada (Pi)
    data_frame["Pi"] = data_frame["pi"].cumsum()

    # Se retorna el dataFrame
    return data_frame


# Se crea una lista de edades
edades_alumnos = [19, 29, 19, 22, 23, 19, 30, 19, 19, 19, 20, 20, 20, 18, 22, 19, 34, 34, 21, 21, 22, 28, 29, 19, 20, 19, 25, 28, 21, 22]

# Se almacena en una variable el resultado de la función y se envía como la lista de edades
resultado = analisis_estadistico(edades_alumnos)
print(resultado.to_string(index=False))