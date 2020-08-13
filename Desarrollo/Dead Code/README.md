## Dead Code :volcano:	

El Lava Flow AntiPattern se encuentra comúnmente en sistemas que se originaron como investigación pero terminaron en producción. Se caracteriza por los "flujos" parecidos a laval de versiones de desarrollo previas esparcidas por el panorama del código, que ahora se han endurecido en una masa de código similar al basalto, inamovible y generalmente inútil de la que nadie puede recordar mucho, si es que hay algo.

Este es el resultado de tiempos de desarrollo anteriores (quizás jurásicos) cuando, mientras estaban en un modo de investigación, los desarrolladores probaron varias formas de lograr cosas, generalmente con prisa por ofrecer algún tipo de demostración, lanzando así prácticas de diseño de sonido a los vientos y sacrificando documentación.

### Antecedentes 

En una expedición de minería de datos, comenzamos a buscar información para desarrollar una interfaz estándar para un tipo particular de sistema. El sistema que estábamos extrayendo era muy similar a los que esperábamos que eventualmente admitieran el estándar en el que estábamos trabajando. También era un sistema de investigación y muy complejo. Mientras profundizamos en él, entrevistamos a muchos de los desarrolladores sobre ciertos componentes de la enorme cantidad de páginas de código impresas para nosotros.

Una y otra vez, recibimos la misma respuesta: "No sé para qué es esa clase; fue escrita antes de que yo llegara". Gradualmente nos dimos cuenta de que entre el 30 y el 50 por ciento del código real que comprendía este complejo sistema no era entendido ni documentado por nadie que trabajara en él.

Además, mientras lo analizamos, nos enteramos de que el código cuestionable realmente no tenía ningún propósito en el sistema actual; más bien, estaba allí de intentos o enfoques anteriores de desarrolladores que se habían ido. El personal actual, aunque muy inteligente, se mostraba reacio a modificar o eliminar el código que no escribían o no conocían el propósito, por temor a romper algo y no saber por qué o cómo solucionarlo.

En este punto, comenzamos a llamar a estas manchas de código "lava", refiriéndonos a la naturaleza fluida en la que se originaron en comparación con la dureza del basalto y la dificultad para eliminarlo una vez que se solidificó. De repente, nos dimos cuenta de que habíamos identificado un AntiPattern potencial.

Casi un año después, y después de varias expediciones de minería de datos y esfuerzos de diseño de interfaces, habíamos encontrado el mismo patrón con tanta frecuencia que habitualmente nos referíamos a Lava Flow en todo el departamento.

### **Sintomas Y Consecuencias:**

* Variables injustificables frecuentes y fragmentos de código en el sistema.

* Funciones, clases o segmentos complejos indocumentados que parecen importantes y que no se relacionan claramente con la arquitectura del sistema.

* Arquitectura de sistema muy flexible y "en evolución".

* Bloques completos de código comentado sin explicación ni documentación.

* Muchas áreas de código "en proceso de cambio" o "por reemplazar".
 
* Código no utilizado (muerto), recién dejado.

* Interfaces no utilizadas, inexplicables u obsoletas ubicadas en archivos de encabezado.

* Si no se elimina el código de Lava Flow existente, puede continuar proliferando a medida que el código se reutiliza en otras áreas.

* Si no se controla el proceso que conduce a Lava Flow, puede haber un crecimiento exponencial ya que los desarrolladores sucesivos, demasiado apresurados o intimidados para analizar los flujos originales, continúan produciendo nuevos flujos secundarios mientras tratan de trabajar alrededor de los originales. el problema.

* A medida que los flujos se componen y endurecen, rápidamente se vuelve imposible documentar el código o comprender su arquitectura lo suficiente como para realizar mejoras.

### **Causas:**

* El código de I + D se pone en producción sin pensar en la gestión de la configuración.

* Distribución incontrolada de código inacabado. Implementación de varios enfoques de prueba para implementar alguna funcionalidad.

* Código escrito de un solo desarrollador (lobo solitario).

* Falta de gestión de la configuración o cumplimiento de las políticas de gestión de procesos.

* Falta de arquitectura o desarrollo no impulsado por la arquitectura. Esto es especialmente frecuente en equipos de desarrollo altamente transitorios.

* Proceso de desarrollo repetitivo. A menudo, los objetivos del proyecto de software no están claros o cambian repetidamente. Para hacer frente a los cambios, el proyecto debe volver a trabajar, retroceder y desarrollar prototipos. En respuesta a los plazos de demostración, existe una tendencia a realizar cambios apresurados en el código sobre la marcha para resolver problemas inmediatos. El código nunca se limpia, dejando la consideración arquitectónica y la documentación pospuesta indefinidamente.

* Cicatrices arquitectónicas. A veces, los compromisos arquitectónicos que se hacen durante el análisis de requisitos no funcionan después de cierto grado de desarrollo. La arquitectura del sistema puede reconfigurarse, pero estos errores en línea rara vez se eliminan. Es posible que ni siquiera sea factible comentar código innecesario, especialmente en entornos de desarrollo modernos donde cientos de archivos individuales comprenden el código de un sistema. "¿Quién va a buscar en todos esos archivos? ¡Solo tienes que vincularlos!"

### **Refactored Solution:**

Solo hay una forma infalible de prevenir Lava Flow AntiPattern: asegúrese de que la arquitectura de sonido precede al desarrollo del código de producción. Esta arquitectura debe estar respaldada por un proceso de gestión de la configuración que garantice el cumplimiento de la arquitectura y se adapte a la "misión lenta" (requisitos cambiantes).

Si la consideración de la arquitectura no se modifica por adelantado, en última instancia, se desarrolla un código que no es parte de la arquitectura de destino y, por lo tanto, es redundante o está muerto. Con el tiempo, el código muerto se vuelve problemático para el análisis, la prueba y la revisión.

En los casos en los que Lava Flow ya existe, la cura puede ser dolorosa. Un principio importante es evitar cambios de arquitectura durante el desarrollo activo. En particular, esto se aplica a la arquitectura computacional, las interfaces de software que definen la solución de integración de sistemas. La gerencia debe posponer el desarrollo hasta que se haya definido una arquitectura clara y se haya difundido a los desarrolladores.

La definición de la arquitectura puede requerir una o más actividades de descubrimiento del sistema. El descubrimiento del sistema es necesario para localizar los componentes que realmente se utilizan y son necesarios para el sistema. El descubrimiento del sistema también identifica aquellas líneas de código que se pueden eliminar de forma segura. Esta actividad es tediosa; puede requerir las habilidades de investigación de un detective de software experimentado.

A medida que se elimina el código muerto sospechoso, se introducen errores. Cuando esto suceda, resista la tentación de corregir inmediatamente los síntomas sin comprender completamente la causa del error. Estudie las dependencias. Esto le ayudará a definir mejor la arquitectura de destino.

Para evitar Lava Flow, es importante establecer interfaces de software a nivel de sistema que sean estables, bien definidas y claramente documentadas. La inversión inicial en interfaces de software de calidad puede producir grandes dividendos a largo plazo en comparación con el costo de eliminar los glóbulos endurecidos del código Lava Flow.

Herramientas como el sistema de control de código fuente (SCCS) ayudan en la gestión de la configuración. SCCS se incluye con la mayoría de los entornos Unix y proporciona una capacidad básica para registrar historiales de actualizaciones en archivos controlados por configuración.

### **Ejemplo:**

Recientemente participamos en un sitio de expedición de minería de datos donde intentamos identificar interfaces evolutivas que resultaron de arquitecturas de interfaz preliminares que originamos y estábamos en proceso de actualización.

El sistema que extrajimos fue dirigido porque los desarrolladores habían utilizado nuestra arquitectura inicial de una manera única que nos fascinó: esencialmente, construyeron un servicio de cuasi-evento a partir de nuestro marco genérico entre aplicaciones.

Mientras estudiábamos su sistema, encontramos grandes segmentos de código que nos desconcertaron. Estos segmentos no parecían contribuir a la arquitectura general que esperábamos encontrar. Eran algo incohesivos y muy escasamente documentados, si es que lo hicieron.

Cuando preguntamos a los desarrolladores actuales sobre algunos de estos segmentos, la respuesta fue: "¿Ah, eso? Bueno, ya no usamos ese enfoque. Reggie estaba intentando algo, pero se nos ocurrió una manera mejor. Supongo que algunos de los otros el código puede depender de esas cosas, así que no eliminamos nada ". A medida que profundizamos en el asunto, nos enteramos de que Reggie ya ni siquiera estaba en el sitio y no había estado allí durante algún tiempo, por lo que los segmentos de código tenían varios meses.

Después de dos días de examen de código, nos dimos cuenta de que la mayoría del código que comprendía el sistema era probablemente similar al código que ya examinamos: completamente Lava Flow en la naturaleza.

Recolectamos muy poco que nos ayudó a articular cómo se construyó realmente su arquitectura; por lo tanto, era casi imposible extraerlo. En este punto, esencialmente dejamos de intentar extraer el código y, en cambio, nos enfocamos en las explicaciones del desarrollador actual de lo que estaba "realmente" sucediendo, con la esperanza de codificar de alguna manera su trabajo en extensiones de interfaz que pudiéramos incorporar en nuestras próximas revisiones de nuestro marco de trabajo entre aplicaciones.

Una solución fue aislar a la única persona clave que mejor entendía el sistema que habían desarrollado y luego escribir IDL conjuntamente con esa persona. En la superficie, el propósito de la IDL que estábamos escribiendo conjuntamente era apoyar una manifestación de crisis que estaba a semanas de distancia.

Al utilizar Fire Drill Mini-AntiPattern, pudimos lograr que los desarrolladores de sistemas validaran nuestro IDL usándolo para construir rápidamente un contenedor CORBA para su producto para la demostración. Mucha gente perdió mucho sueño, pero la demostración salió bien. Por supuesto, esta solución tenía un efecto secundario: terminamos con la interfaz, en IDL, que nos habíamos propuesto descubrir en primer lugar.


[Referencas](https://sourcemaking.com/antipatterns/lava-flow)