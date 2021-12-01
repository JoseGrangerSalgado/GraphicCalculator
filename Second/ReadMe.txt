En este documento explicamos para que sirve cada archivo en nuestra tarea.

En la carpeta de Static, se guarda el CSS que se usa en nuestra pagina html y tambien en una carpeta de graphs, se guarda el graph 
que se crea cada vez que mandas una nueva ecuacion.

En la carpeta de templates se encuentra el template html que usamos para crear nuestra pagina web.

En la carpeta de test_docs, se encuentran dos documentos txt en donde se van a guardar las pruebas una vez que se ejecuten 
los archivos python en donde se realizan las pruebas (Selenium, y Peticiones al API).

En el archivo de api_test.py se realizan las pruebas al endpoint que usamos para generar las graficas, puedes poner el numero de pruebas que 
se requieran. Se va a escribir el numero de la prueba, el Status Code resultante y el tiempo que tomo en responder.
(Advertencia :  Se necesita correr webpage.py para que sirva este archivo)

Seguido de esto esta el chromedriver.exe, un archivo cual requiere Selenium para poder realizar las pruebas en un web browser.
(Si no usas Chrome, descarga el driver dependiendo de tu web browser y modifica la linea 8 del codigo para que tenga acceso al driver)

Tenemos ademas de esto, dos archivos multiprocess, el primer archivo corre la pagina y realiza las pruebas de Selenium al mismo tiempo.
En el segundo archivo, se corre la pagina y las pruebas de API.
(Toman unos segundos en empezar las pruebas de Selenium)

En el archivo test_web.py, se realizan las pruebas de Selenium donde el software automaticamente introduce varias ecuaciones en nuestra pagina
y guarda los resultados en un archivo txt (selenium_tests.txt).
(Advertencia :  Se necesita correr webpage.py para que sirva este archivo)

Finalmente, tenemos el archivo webpage.py donde creamos el servidor de Flask y a partir de esto, usando la ecuacion que introduzca el usuario
en la pagina, usamos el metodo de newton e eval para poder regresar la grafica y varias estadisticas en una tabla.
(Este archivo puede correr independientemente.)


