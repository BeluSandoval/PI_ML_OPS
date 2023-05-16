<p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>

# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>

# <h1 align=center>**`Machine Learning Operations (MLOps)`**</h1>

<p align="center">
<img src="https://user-images.githubusercontent.com/67664604/217914153-1eb00e25-ac08-4dfa-aaf8-53c09038f082.png"  height=300>
</p>

¡Bienvenidos al primer proyecto individual de la etapa de labs! Soy Belén Sandoval Pinget, alumna de Soy Henry y en esta ocasión, tengo que realizar un trabajo situándome en el rol de un ***MLOps Engineer***.  

<hr>  

<br/>

## **Contexto**

El cliente nos solicitó y entregó un conjunto de datos, con el objetivo de que los procesemos y creemos un sistema de recomendación.


<br/>

## **Objetivo**:



El objetivo principal de este proyecto es la creación de una API que consuma datos creados a para desarrollar e implementar un sistema de recomendación de películas basado en el contenido aprovechando los datos de un conjunto completo de datos de películas. El proyecto pretende alcanzar los siguientes objetivos específicos:

+ **`Transformación y limpieza de datos`**: aplicar técnicas de extracción, transformación y carga (ETL) para preprocesar y limpiar el conjunto de datos de películas.

+ **`Análisis exploratorio de datos (EDA)`**: realizar un análisis exploratorio de datos en profundidad para obtener información sobre los atributos de la película, como el título, la descripción general y los géneros.
  
+ **`Desarrollo de API`**: diseñar e implementar un conjunto de funciones para los endpoint que serán consumidos en la API. Luego esta se desplegará a través de Render para que se pueda consumir desde de la web. 

+ **`Creación de un modelo de recomendación`**: entrenar nuestro modelo de machine learning para armar un sistema de recomendación de películas. Debe ser deployado como una función adicional de la API anterior y debe llamarse get_recommendation(titulo: str).

<br/>

## **Procesamiento de datos:** 

[ETL](https://github.com/BeluSandoval/PI_ML_OPS/blob/main/ETL.ipynb)

+ Algunos campos, como belongs_to_collection, production_companies y otros (ver diccionario de datos) están anidados, esto es o bien tienen un diccionario o una lista como valores en cada fila, ¡deberán desanidarlos para poder y unirlos al dataset de nuevo hacer alguna de las consultas de la API! O bien buscar la manera de acceder a esos datos sin desanidarlos.

+ Los valores nulos de los campos revenue, budget deben ser rellenados por el número 0.

+ Los valores nulos del campo release date deben eliminarse.

+ De haber fechas, deberán tener el formato AAAA-mm-dd, además deberán crear la columna release_year donde extraerán el año de la fecha de estreno.

+ Crear la columna con el retorno de inversión, llamada return con los campos revenue y budget, dividiendo estas dos últimas revenue / budget, cuando no hay datos disponibles para calcularlo, deberá tomar el valor 0.

+ Eliminar las columnas que no serán utilizadas, video,imdb_id,adult,original_title,vote_count,poster_path y homepage.

## **Análisis Exploratorio de Datos**

[EDA](https://github.com/BeluSandoval/PI_ML_OPS/blob/main/EDA.ipynb)

## **Desarrollo API**

 [main.py](https://github.com/BeluSandoval/PI_ML_OPS/blob/main/main.py)

Deben crear 6 funciones para los endpoints que se consumirán en la API, recuerden que deben tener un decorador por cada una (@app.get(‘/’)).

+ **`Función 1:`** def peliculas_mes(mes): 'Se ingresa el mes y la funcion retorna la cantidad de peliculas que se estrenaron ese mes (nombre del mes, en str, ejemplo 'enero') historicamente'.
return {'mes':mes, 'cantidad':respuesta}

+ **`Función 2:`** def peliculas_dia(dia): 'Se ingresa el dia y la funcion retorna la cantidad de peliculas que se estrenaron ese dia (de la semana, en str, ejemplo 'lunes') historicamente'.
return {'dia':dia, 'cantidad':respuesta}

+ **`Función 3:`** def franquicia(franquicia): 'Se ingresa la franquicia, retornando la cantidad de peliculas, ganancia total y promedio'.
 return {'franquicia':franquicia, 'cantidad':respuesta, 'ganancia_total':respuesta, 'ganancia_promedio':respuesta}

+ **`Función 4:`** def peliculas_pais(pais): 'Ingresas el pais, retornando la cantidad de peliculas producidas en el mismo'. 
return {'pais':pais, 'cantidad':respuesta}

+ **`Función 5:`** def productoras(productora): 'Ingresas la productora, retornando la ganancia total y la cantidad de peliculas que produjeron'.
return {'productora':productora, 'ganancia_total':respuesta, 'cantidad':respuesta}

+ **`Función 6:`** def retorno(pelicula): 'Ingresas la pelicula, retornando la inversion, la ganancia, el retorno y el año en el que se lanzo'. 
return {'pelicula':pelicula, 'inversion':respuesta, 'ganacia':respuesta,'retorno':respuesta, 'anio':respuesta}


<br/>


## **Deployment API**

El despliegue se realizó a través de Render en el siguiente enlace [PI-MLOpsEngineer](https://pimlops-yelj.onrender.com/docs)



<br/>


## **Modelo de Recomendación**

[recomendacion.ipynb](https://github.com/BeluSandoval/PI_ML_OPS/blob/main/Recomendacion.ipynb)

Para el sistema de recomendación se utilizó el modelo de "similitud de coseno". El nombre de la función se puede encontrar en la misma interfaz API que una séptima consulta, llamada get_recomendation(title), donde ingresa el título de una película y devuelve una lista de 5 películas recomendadas según ese título ingresado. Debido al gran tamaño del archivo generado luego del procesamiento, para poder ejecutar el deployment en Render, se redujo el número de registros a 1000, los cuales se guardan en un archivo .pickle llamado [similarity_matrix.pickle](https://github.com/BeluSandoval/PI_ML_OPS/blob/main/similarity_matrix.pickle). No obstante, para mostrar el funcionamiento de la función, hay una [lista de 5 peliculas](https://github.com/BeluSandoval/PI_ML_OPS/blob/main/5_peliculas.txt) incluidas en el modelo.

<br/>


## **Video explicación:**
[link](https://youtu.be/EqOeW7UjpiA)


**`Video`**: Necesitas que al equipo le quede claro que tus herramientas funcionan realmente! Haces un video mostrando el resultado de las consultas propuestas y de tu modelo de ML entrenado!

<sub> **Spoiler**: El video NO DEBE durar mas de ***7 minutos*** y DEBE mostrar las consultas requeridas en funcionamiento desde la API** y una breve explicacion del modelo utilizado para el sistema de recomendacion. <sub/>

<br/>


## **Fuente de datos**

+ [Dataset](https://drive.google.com/file/d/1Rp7SNuoRnmdoQMa5LWXuK4i7W1ILblYb/view?usp=sharing): Archivo con los datos que requieren ser procesados, tengan en cuenta que hay datos que estan anidados (un diccionario o una lista como valores en la fila).
+ [Diccionario de datos](https://docs.google.com/spreadsheets/d/1QkHH5er-74Bpk122tJxy_0D49pJMIwKLurByOfmxzho/edit#gid=0): Diccionario con algunas descripciones de las columnas disponibles en el dataset.


  
<br/>

## **Deadlines importantes**

+ Apertura de formularios de entrega de proyectos: **Lunes 15, 10:00 hs gmt -3**

+ Cierre de formularios de entrega de proyectos: **Martes 16, 16:00hs gmt-3**
  
+ Demo: **Martes 16, 16:00hs gmt-3*** 
