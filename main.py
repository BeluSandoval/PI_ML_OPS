from fastapi import FastAPI
import pandas as pd
import pickle

app = FastAPI()

# http://127.0.0.1:8000 

@app.get("/")
def index():
    return 'Bienvenidos'

@app.get('/about')
async def about():
    return 'Soy Henry PI-MLOPs'

# Importamos dataset
df = pd.read_csv(r'df_final.csv')
Df = pd.read_csv(r'Df_recomendacion.csv')
df['release_date'] = pd.to_datetime(df['release_date'], format='%Y-%m-%d', errors='coerce')

with open('similarity_matrix.pickle', 'rb') as f:
    cosine_sim = pickle.load(f)

#Consultas

#1
@app.get('/peliculas_mes/{mes}')
async def peliculas_mes(mes:str):
    
    # Creamos un diccionario para convertir nombres de meses a números
    meses = {'enero': 1, 'febrero': 2, 'marzo': 3, 'abril': 4, 'mayo': 5, 'junio': 6,
         'julio': 7, 'agosto': 8, 'septiembre': 9, 'octubre': 10, 'noviembre': 11, 'diciembre': 12}
    # Convertimos el mes a su representación numérica utilizando el diccionario
    mes_num = meses[mes.lower()]
    
    # Filtramos las filas del dataframe por el mes correspondiente
    peliculas_mes = df.loc[df['release_date'].dt.month == mes_num]
    
    # Contamos el número de filas filtradas y devolvemos el resultado como un diccionario
    respuesta = str(len(peliculas_mes))
    return {'mes': mes, 'cantidad': respuesta}

#2  
@app.get('/peliculas_dia/{dia}')
async def peliculas_dia(dia:str):
    
    dias_semana = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo']
    if dia.lower() not in dias_semana:
        return {'dia': dia, 'cantidad': 0}
    else:
        dia_df = df[df['day_of_week'] == dia.lower()]
        cantidad = len(dia_df)
        return {'dia': dia, 'cantidad': cantidad}
    
#3
@app.get('/franquicia/{franquicia}')
async def franquicia(franquicia:str):
    # Filtrar el DataFrame original para incluir solo filas con información sobre la franquicia
    franquicia_df = df[(df['belongs_to_collection'].notna()) & (df['belongs_to_collection'].str.contains(franquicia))]
    
    # si hay nulos
    if franquicia_df.empty:
        return "No se encontro la franquicia"
    
    # Obtener la cantidad de películas, la ganancia total y la ganancia promedio
    cantidad = franquicia_df.shape[0]
    ganancia_total = franquicia_df['revenue'].sum()
    ganancia_promedio = ganancia_total / cantidad
    
    # Retornar la información en un diccionario
    return {'franquicia': franquicia, 'cantidad': cantidad, 'ganancia_total': ganancia_total, 'ganancia_promedio': ganancia_promedio}

#4
@app.get('/peliculas_pais/{pais}')
async def peliculas_pais(pais:str):
    # Contar el número de películas que se hicieron en el país especificado
    num_peliculas = len(df[df['production_countries'].str.contains(pais)])
    
    # Crear un diccionario que contenga el país y el número de películas
    return {'pais': pais, 'cantidad': num_peliculas}

#5
@app.get('/productoras/{productora}')
async def productoras(productora:str):    
    df_filtrado = df[df['production_companies'].str.contains(productora, na=False)]
    ganancia_total = df_filtrado['revenue'].sum()
    cantidad = len(df_filtrado)
    return {'productora': productora, 'ganancia_total': ganancia_total, 'cantidad': cantidad}

#6
@app.get('/retorno/{pelicula}')
async def retorno(pelicula:str):
    # Filtro la información de la película en base a su título
    pelicula_info = df[df['title'] == pelicula].iloc[0]
    
    # Obtengo la inversión, ganancia, retorno y año de lanzamiento de la película
    inversion = int(pelicula_info['budget'])
    ganancia = int(pelicula_info['revenue'])
    retorno = int(pelicula_info['return'])
    anio = int(pelicula_info['release_year'])
    
    # Retorno la información en un diccionario
    return {'pelicula': pelicula, 'inversion': inversion, 'ganancia': ganancia, 'retorno': retorno, 'anio': anio}

# ML. MODELO DE RECOMENDACIÓN
@app.get('/recomendacion/{titulo}')
def recomendacion(titulo:str):
    # Buscar la fila correspondiente al título de la película
    idx = Df.index[Df["title"].str.lower() == titulo.lower()].tolist()
    if len(idx) == 0:
        return "Película no encontrada"
    else:
        idx = idx[0]
    
    # Calcular la similitud de la película con todas las demás películas
    sim_scores = list(enumerate(cosine_sim[idx]))
    
    # Ordenar las películas según su similitud y seleccionar las 5 más similares
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]
    
    # Obtener los índices de las películas recomendadas
    movie_indices = [i[0] for i in sim_scores]
    
    # Devolver los títulos de las películas recomendadas
    return list(Df["title"].iloc[movie_indices])
   