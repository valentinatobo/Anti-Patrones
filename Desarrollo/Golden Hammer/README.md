## Golden Hammer :hammer:

Un equipo de desarrollo de software ha obtenido un alto nivel de competencia en una solución o producto de un proveedor en particular, al que nos referiremos aquí como el Martillo de Oro. Como resultado, cada nuevo producto o esfuerzo de desarrollo se considera algo que se resuelve mejor con él. En muchos casos, el martillo de oro es un desajuste para el problema, pero se dedica un esfuerzo mínimo a explorar soluciones alternativas.

Este AntiPattern da como resultado la aplicación incorrecta de una herramienta o concepto preferido. Los desarrolladores y gerentes se sienten cómodos con un enfoque existente y no están dispuestos a aprender y aplicar uno que sea más adecuado. Esto se caracteriza por la mentalidad común de "nuestra base de datos es nuestra arquitectura", particularmente común en la comunidad bancaria mundial.

### Antecedentes 

Este es uno de los AntiPatterns más comunes en la industria. Con frecuencia, un proveedor, específicamente un proveedor de bases de datos, abogará por el uso de su creciente suite de productos como una solución para la mayoría de las necesidades de una organización. Dado el gasto inicial de adoptar una solución de base de datos específica, dicho proveedor a menudo proporciona extensiones a la tecnología que han demostrado que funcionan bien con sus productos implementados a precios muy reducidos.

### **Sintomas y Consecuencias:**

* La arquitectura del sistema se describe mejor mediante un conjunto de herramientas de producto, conjunto de aplicaciones o proveedor en particular.

* Los desarrolladores debaten los requisitos del sistema con los analistas del sistema y los usuarios finales, con frecuencia abogan por requisitos que son fácilmente adaptados por una herramienta particular y alejándolos de las áreas donde la herramienta adoptada es insuficiente.

* Los desarrolladores quedan aislados de la industria. Demuestran una falta de conocimiento y experiencia con enfoques alternativos.

* Los productos existentes dictan el diseño y la arquitectura del sistema.

* El nuevo desarrollo depende en gran medida de un producto o tecnología de un proveedor específico.

### **Causas:**

* Varios casos de éxito utilizando la misma herramienta.

* Gran inversión en formación y experiencia en un producto o tecnología concreta.

* El equipo IT está aislado de la industria y de otras compañías.

* Confianza en las características de productos propietarios que no están disponibles en otros productos de la industria.


### **Refactored Solution:**

La solución planteada plantea un aspecto filosófico, así como un cambio en el proceso de desarrollo.  Filosóficamente, una organización necesita desarrollar un compromiso en la exploraciones de nuevas tecnologías.

Sin este compromiso, existe el peligro de depender demasiado tiempo de una tecnología especifica o conjunto de herramientas. Esta solución requiere un enfoque en dos frentes: un mayor compromiso de los gestores en el crecimiento personal de los desarrolladores, junto a una estrategia de desarrollo que requiere fronteras para permitir la migración de tecnologías.

Los sistemas software deben ser diseñados y desarrollados con los límites bien definidos que permitan la sustitución de componentes software. Un componente debe aislar las características dentro de su implementación.

Si se desarrolla marcando estos límites, las interfaces se convierten en puntos en los que el software utilizado puede ser reemplazado por una nueva implementación, sin afectar a otros componentes del sistema. Esto es complicado con sistemas software rígidos que no aportan en el proceso de cambio.

Además, los desarrolladores software necesitan estar a la última en tendencias tecnologías, tanto dentro de la organización como en el sector del software. Esto se puede conseguir a través de actividades que fomentan el intercambio del conocimiento. Por ejemplo, los desarrolladores pueden hacer grupos para discutir apartados técnicos que puedan tener un impacto en el futuro de la  organización.

También es interesante invertir en el estudio de libros sobre software, analizando las publicaciones y encontrando nuevos paradigmas que fomenten una atmósfera de intercambio de ideas y nuevos enfoques.

Los desarrolladores pueden establecer redes informales de personas con mentalidad tecnológica para investigar nuevas tecnologías y soluciones. Las conferencias/meetups del sector también son una excelente forma de contactar con personas y proveedores y mantenerse informados sobre hacia dónde se dirigen las industrias y qué nuevas soluciones están disponibles para los desarrolladores.

El código flexible y reutilizable requiere una inversión en su desarrollo inicial; de lo contrario, no se lograrán beneficios a largo plazo. El peligro de depender demasiado de una tecnología específica o de un conjunto de herramientas de proveedores es un riesgo potencial en el desarrollo del producto o proyecto. Los programas de investigación internos que desarrollan prototipos de prueba de concepto son efectivos para probar la viabilidad de incorporar tecnologías abiertas de una manera menos arriesgada en un esfuerzo de desarrollo aceptable.

Otra forma de eliminar o evitar el anti-patrón es fomentar la contratación de personas de diferentes áreas y de diferentes entornos. Los equipos se benefician de tener una base de experiencia más amplia para utilizar en el desarrollo de soluciones. La contratación de un equipo de base de datos cuyos miembros tengan experiencia en el uso del mismo producto de base de datos limita en gran medida el espacio de solución probable, en comparación con un equipo similar cuya experiencia abarca una amplia gama de soluciones de tecnología de bases de datos.

Finalmente, la organización debe invertir activamente en el desarrollo profesional de los desarrolladores de software, así como impartir recompensas a los desarrolladores  que toman iniciativas para mejorar su propio trabajo.

### **Ejemplo:**

Un ejemplo común de Golden Hammer es un entorno centrado en la base de datos sin una arquitectura adicional, excepto aquella que proporciona el proveedor de la base de datos. En ese entorno, se supone el uso de una base de datos particular incluso antes de que haya comenzado el análisis orientado a objetos. Como tal, el ciclo de vida del software frecuentemente comienza con la creación de un diagrama entidad-relación (E-R) que se produce como un documento de requisitos con el cliente.

Esto es frecuentemente negativo, porque el diagrama E-R finalmente se usa para especificar los requisitos de la base de datos; y detallar la estructura de un sub-sistema antes de comprender y modelar el sistema presupone que el impacto de los requisitos reales del cliente en el diseño del sistema es mínimo.

La recopilación de requisitos debería permitir a los desarrolladores del sistema comprender las necesidades del usuario en la medida en que el comportamiento de la solución sea entendido por el usuario como una caja negra. Probablemente, muchos sistemas están diseñados para satisfacer los requisitos del usuario sin utilizar ninguna base de datos. Sin embargo, con el Golden Hammer, tales posibilidades se descartan por adelantado, lo que lleva a que cada problema incorpore un elemento de base de datos.

Con el tiempo, la organización puede desarrollar varios productos centrados en la base de datos que podrían haberse implementado como sistemas independientes. La base de datos se convierte en la base de la inter-conectividad entre las aplicaciones y gestiona la distribución y el acceso compartido a los datos. Además, muchos problemas de implementación se abordan mediante el uso de características de la propia base de datos acoplándonos a ella y comprometiendo futuras migraciones para que sean paralelas al desarrollo de una tecnología de la base de datos de implementación.

En algún momento, puede ser necesario operar con sistemas que no comparten la misma arquitectura centrada en la base de datos o que se implementan utilizando una base de datos diferente que puede no permitir el acceso irrestricto a su información. De repente, el desarrollo se vuelve extremadamente costoso ya que las conexiones únicas y de propósitos especiales se crean para “tender puentes” entre sistemas únicos. Sin embargo, si se reflexiona sobre el problema antes de que la situación se salga de control, se puede desarrollar un core común, donde los productos elegidos para áreas particulares se seleccionan en función de las especificaciones de interfaz estándar.


[Referencas](https://sourcemaking.com/antipatterns/golden-hammere)