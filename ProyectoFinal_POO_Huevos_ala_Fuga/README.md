<h1 style="font-family: 'Arial'; font-size:30px;">Proyecto Final de POO Huevos a la Fuga</h1>

<h2 style="font-family: 'Arial'; font-size:24px; color:">Integrantes</h2>
<ul >
    <li>Miguel Ángel Salazar Orrego</li>
    <li>Luisa Fernanda Espinal Montoya</li>
    <li>José Ángel Sánchez Martínez</li>
    <li>Zharick Dayana Vasquez Valenzuela</li>
</ul>

<h2 style="font-family: 'Arial'; font-size:20px">Descripción</h2>

<h3 style="font-family: 'Arial'; font-size:20px">Huevos a la Fuga</h3>

<p >En "Huevos a la Fuga", el jugador controla un huevo que ha caído de la nevera y descubre que la cocina es un lugar lleno de peligros. La misión del jugador es guiar al huevo esquivando obstáculos para así llegar a la ventana y escapar. El huevo cuenta con tres vidas representadas por su cáscara. Cada vez que choca contra un obstáculo, se forma una grieta debilitando su estructura. Si acumula tres grietas, el huevo se rompe por completo, convirtiéndose en un huevo revuelto y el juego termina.</p>

<h3 style="font-family: 'Arial'; font-size:20px">Dinámica del Juego</h3>

<p>El juego es una plataforma 2D con desplazamiento lateral donde el jugador debe moverse y saltar a través de la cocina esquivando peligros y utilizando power-ups para llegar a la meta.</p>
<ul>
<li>Movimiento: El huevo puede moverse a la izquierda, derecha y saltar.</li>

<li>Sistema de daño: Cada vez que el huevo choca contra un obstáculo, se formarán grietas.Si acumula tres grietas, el huevo se rompe por completo, convirtiéndose en un huevo revuelto. </li>
</ul>
<h3 style="font-family: 'Arial'; font-size:20px">Niveles y Progresión</h3>

<p>El juego tendrá tres niveles con dificultad creciente:</p>
<ol>
<li style="list-style-type: decimal;">Cocina Inicial: El huevo cae de la nevera y aprende los controles básicos. Obstáculos simples como charcos de aceite.</li>

<li style="list-style-type: decimal;">Zona de Cocción: Se introducen sartenes calientes y utensilios en movimiento.</li>

<li style="list-style-type: decimal;">Gran Escape: El chef aparece y persigue al huevo mientras este intenta alcanzar la ventana para escapar.</li>

</ol>
<p>Cada nivel tendrá un tiempo límite, lo que obliga al jugador a tomar decisiones rápidas.</p>

<h3 style="font-family: 'Arial'; font-size:20px">Obstáculos y Peligros</h3>
<ul>
<li>Sartenes calientes: Contacto directo causa una derrota instantánea.</li>

<li>Charcos de aceite: Provoca resbalones y movimientos incontrolables.</li>

<li>Chef malvado: Persigue al huevo en los niveles avanzados e intenta atraparlo.</li>
</ul>
<h3 style="font-family: 'Arial'; font-size:20px">Power-Ups</h3>

Para ayudar al jugador, el huevo puede recolectar power-ups:
<ul>
<li>Cáscara extra: Reduce el daño de los choques por un tiempo limitado.</li>

<li>Turbo: Aumenta la velocidad del huevo durante 3 segundos.</li>

<li>Papel de aluminio: Hace al huevo invulnerable durante 3 segundos.</li>
</ul>

<h3 style="font-family: 'Arial'; font-size:20px">Condiciones de Victoria y Derrota</h3>
<ul>
<li>Victoria: El huevo gana si logra llegar a la ventana y escapar.

<li>Derrota: El jugador pierde si:</li>
    <ul>
        <li>El huevo se rompe completamente.</li>
        <li>El chef lo atrapa.</li>
        <li>Cae en una sartén caliente.</li>
    </ul>
</ul>
<h3 style="font-family: 'Arial'; font-size:20px">Persistencia y Tabla de Clasificación</h3>
<p>El juego guardará los resultados de cada partida:</p>
<ul>
<li>Registro de puntajes: Se guardará el tiempo que tarda el jugador en escapar.</li> 
<li>Tabla de clasificación: Mostrará los mejores tiempos de los jugadores.</li>
</ul>
<h3 style="font-family: 'Arial'; font-size:20px">Tecnologías y Desarrollo</h3>
<ul>
<li>PyGame: Para la programación del juego, animaciones y detección de colisiones.</li>
<li>Sistema de físicas simple: Para manejar la gravedad y los saltos.</li>
<li>Archivos JSON: Para guardar el progreso y los puntajes de los jugadores.</li>
</ul>

<h2 style="font-family: 'Arial'; font-size:24px">Instalación</h2>

```bash
pip install pygame
```

<h2 style="font-family: 'Arial'; font-size:24px">Ejecutar Aplicación</h2>

```bash
python run.py
```
