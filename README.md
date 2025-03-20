<h1 align="center"> Estimación del clima mediante nubes </h1>

<h2>Introducción </h2>

<p>Este programa cumple la función de interpretar una imagen del cielo para detectar el tiempo o clima mediante el calculo de la cantidad de area tomada por las nubes y el color de estas. </p>

<h2>Herramientas <h2>

<p>Se utilizó python con la agregación de las siguientes librerías: </p>
<ul>
    <li> opencv-python : para manejar los filtros y edición de la imagen</li>
    <li> numpy : para utilizar arreglos</li>
    <li> matplotlib : para mostrar las imagenes</li>
</ul>

<h2>Descripción del proceso</h2>

<p>Primeramente, La imagen pasa por un filtro que localiza cierto rango de colores azules en busca de, posteriormente, eliminarlos para enfocar solo las nubes. Luego, se pasa esta imagen a otra nueva en escala de grises para calcular más facilmente la intensidad de color de las nubes. </p>
<p>Con la imagen donde solo se mantuvieron las nubes, se calcula el área en que las nubes estan presentes, obteniendo el procentaje que toman de imagen para determinar lo nublado que está el cielo. Mientras que con la imagen de escala de grises se calcula el promedio de intensidad del color de las nubes para determinar si, en caso de estar con gran cantidad de nubes, está tambien una tormenta.  </p>
<p>Finalmente, se muestran:</p>
<ul>
    <li>La imagen original</li>
    <li>La imagen donde solo se mantienen las nubes</li>
    <li>La imagen donde solo se mantienen las nubes pero en escala de grises</li>
    <li>La imagen original</li>
    <li>El área que las nubes toman en la imagen en porcentaje</li>
    <li>El tono promedio del color de las nubes (de 0 a 255)</li>
    <li>El clima estimado tras la evaluación</li>
</ul>

<h2>Como usarlo </h2>
<p>Primeramente se debe subir la imagen del cielo que se quiere utilizar a al carperta "img" y poner la ruta ("img/nombre_de_la_imagen") hacia dicha iamgen en donde se indica en el inicio del código. Luego, solo ejecutar el código. </p>


