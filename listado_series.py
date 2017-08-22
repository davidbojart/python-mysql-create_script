# VARIABLES #
ruta = "D:/Series/"
lista = os.listdir(ruta)

# FUNCIONES #
def busca_caracter(name_episodio):
    lista = []
    pos_inicial = -1
    try:
        while True:
            # cada vez buscamos desde un caracter más adelante de
            # la última ocurrencia encontrada
            pos_inicial = name_episodio.index('[', pos_inicial+1)
            lista.append(pos_inicial)
            cursor = name_episodio[(lista[0])-1:]
            name_episodio = (name_episodio.replace(cursor, ""))

    except ValueError: # cuando ya no se encuentre la letra
         print "INSERT INTO `videoteca`.`episodio` (`id_episodio`, `nombre_episodio`, `numero_episodio`, `temporada`, `id_serie`) VALUES (NULL, '"+name_episodio+"', '"+numero_episodio+"', '"+temporada+"', (SELECT id_serie FROM videoteca.serie WHERE nombre_serie='"+serie+"'));"   

## Recorre las carpetas para sacar los nombres, temporadas y capitulos de las series ##
         
for serie in lista:
    listado_temporada = os.listdir(ruta+serie)
    # Creamos los inserts de la tabla SERIES
    sys.stdout = open('series.sql', 'a')
	
    print "INSERT INTO `videoteca`.`serie` (`id_serie`, `nombre_serie`, `portada`) VALUES ('NULL', '"+serie+"', '"+serie+".jpg');"
    for temporada in listado_temporada:
        episodios = os.listdir(ruta+serie+"/"+temporada)
		
        for episodio in episodios:
	    #Creamos los inserts en la tabla episodio.
            long_name_serie = len(serie)
            numero_episodio = (episodio[long_name_serie+3:long_name_serie+5]) # Calcula la posicion del numero del episodio
            name_episodio = (episodio[long_name_serie+6:]) # Calcula la posicion del nombre del episodio
            busca_caracter(name_episodio)
        print ""
    sys.stdout.close()# cerramos el fichero
