## Spaghetti Code :spaghetti:	

Spaghetti Code aparece como un programa o sistema que contiene muy poca estructura de software. La codificación y las extensiones progresivas comprometen la estructura del software hasta tal punto que la estructura carece de claridad, incluso para el desarrollador original, si está lejos del software durante un período de tiempo.

Si se desarrolla utilizando un lenguaje orientado a objetos, el software puede incluir una pequeña cantidad de objetos que contienen métodos con implementaciones muy grandes que invocan un único flujo de proceso de múltiples etapas.

Además, los métodos de objeto se invocan de una manera muy predecible y hay un grado insignificante de interacción dinámica entre los objetos del sistema. El sistema es muy difícil de mantener y ampliar, y no hay oportunidad de reutilizar los objetos y módulos en otros sistemas similares.

### Antecedentes 

El Spaghetti Code AntiPattern es el clásico y más famoso AntiPattern; ha existido de una forma u otra desde la invención de los lenguajes de programación. Los lenguajes no orientados a objetos parecen ser más susceptibles a este AntiPattern, pero es bastante común entre los desarrolladores que todavía tienen que dominar completamente los conceptos avanzados que subyacen a la orientación a objetos.

### **Sintomas y Consecuencias:**

* Después de la minería de código, solo algunas partes del objeto y los métodos parecen aptos para su reutilización. Mining Spaghetti Code a menudo puede tener un bajo retorno de la inversión; esto debe tenerse en cuenta antes de tomar una decisión sobre la mía.

* Los métodos están muy orientados al proceso; con frecuencia, de hecho, los objetos se denominan procesos.

* El flujo de ejecución lo dicta la implementación del objeto, no los clientes de los objetos.

* Existen relaciones mínimas entre objetos.

* Muchos métodos de objeto no tienen parámetros y utilizan variables globales o de clase para su procesamiento.

* El patrón de uso de los objetos es muy predecible.

* El código es difícil de reutilizar y, cuando lo es, suele ser mediante la clonación. En muchos casos, sin embargo, el código nunca se considera para su reutilización.

* El talento orientado a objetos de la industria es difícil de retener.
Se pierden los beneficios de la orientación a objetos; la herencia no se usa para extender el sistema; no se utiliza polimorfismo.

* Los esfuerzos de mantenimiento posteriores contribuyen al problema.

* El software alcanza rápidamente un punto de rendimientos decrecientes; el esfuerzo que implica mantener una base de código existente es mayor que el costo de desarrollar una nueva solución desde cero.

### **Causas:**

* Inexperiencia con tecnologías de diseño orientadas a objetos.

* No hay tutoría en su lugar; revisiones de código ineficaces.

* Sin diseño previo a la implementación.

* Con frecuencia, el resultado de los desarrolladores que trabajan de forma aislada.

### **Refactored Solution:**

La refactorización de software (o limpieza de código) es una parte esencial del desarrollo de software. El setenta por ciento o más del costo del software se debe a las extensiones, por lo que es fundamental mantener una estructura de software coherente que admita la extensión.

Cuando la estructura se ve comprometida al admitir requisitos imprevistos, la capacidad del código para admitir extensiones se vuelve limitada y, finalmente, inexistente. Desafortunadamente, el término "limpieza de código" no atrae a los gerentes puntiagudos, por lo que puede ser mejor discutir este tema usando un término alternativo como "inversión en software".

Después de todo, en un sentido muy real, la limpieza de código es el mantenimiento de la inversión en software. El código bien estructurado tendrá un ciclo de vida más largo y podrá soportar mejor los cambios en el negocio y la tecnología subyacente.

Idealmente, la limpieza del código debería ser una parte natural del proceso de desarrollo. A medida que se agrega cada característica (o grupo de características) al código, la limpieza del código debe seguir lo que restaura o mejora la estructura del código. Esto puede ocurrir por horas o por días, dependiendo de la frecuencia de la adición de nuevas funciones.

La limpieza de código también admite la mejora del rendimiento. Por lo general, la optimización del rendimiento sigue la regla 90/10, donde solo el 10 por ciento del código necesita modificación para lograr el 90 por ciento del rendimiento óptimo. Para la programación de un solo subsistema o aplicación, la optimización del rendimiento a menudo implica compromisos con la estructura del código.

El primer objetivo es lograr una estructura satisfactoria; el segundo es determinar mediante medición dónde existe el código de rendimiento crítico; el tercero es introducir cuidadosamente los compromisos estructurales necesarios para mejorar el rendimiento. A veces es necesario revertir los cambios de mejora del rendimiento en el software para proporcionar extensiones esenciales del sistema. Estas áreas merecen documentación adicional para preservar la estructura del software en futuras versiones.

### **Ejemplo:**

Este es un problema frecuente demostrado por personas nuevas en el desarrollo orientado a objetos, que mapean los requisitos del sistema directamente a las funciones, utilizando objetos como un lugar para agrupar funciones relacionadas. Cada función contiene un flujo de proceso completo que implementa completamente una tarea en particular.

Por ejemplo, el segmento de código que sigue contiene funciones como initMenus (), getConnection () y executeQuery (), que ejecutan completamente la operación especificada. Cada método de objeto contiene un único flujo de proceso que realiza todos los pasos en secuencia necesarios para realizar la tarea.

El objeto retiene poca o ninguna información de estado entre invocaciones sucesivas; más bien, las variables de clase son ubicaciones de almacenamiento temporal para manejar los resultados intermedios de un solo flujo de proceso.


[Referencas](https://sourcemaking.com/antipatterns/spaghetti-code)