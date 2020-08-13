## The Blob :zombie:

El Blob se encuentra en diseños donde una clase monopoliza el procesamiento y otras clases encapsulan principalmente datos. Este AntiPattern se caracteriza por un diagrama de clases compuesto por una única clase de controlador compleja rodeada de clases de datos simples. El problema clave aquí es que la mayoría de las responsabilidades se asignan a una sola clase.

En general, el Blob es un diseño de procedimiento, aunque puede representarse mediante notaciones de objetos e implementarse en lenguajes orientados a objetos. Un diseño de procedimiento separa el proceso de los datos, mientras que un diseño orientado a objetos fusiona los modelos de proceso y datos, junto con las particiones.

El Blob contiene la mayor parte del proceso y los demás objetos contienen los datos. Las arquitecturas con Blob han separado el proceso de los datos; en otras palabras, son arquitecturas de estilo procedimental más que orientadas a objetos.

### Antecedentes

¿Recuerdas la película original en blanco y negro The Blob? Quizás viste solo el remake reciente. En cualquier caso, la línea de la historia era casi la misma: una forma de vida alienígena gelatinosa del tamaño de un goteo del espacio exterior de alguna manera llega a la Tierra.

Siempre que la gelatina come (generalmente terrícolas desprevenidos), crece. Mientras tanto, los terrícolas incrédulos entran en pánico e ignoran al científico loco que sabe lo que está sucediendo. Muchas más personas son devoradas antes de que recuperen el sentido. Eventualmente, la Mancha crece tanto que amenaza con acabar con todo el planeta.

La película es una buena analogía para Blob AntiPattern, que se sabe que consume arquitecturas completas orientadas a objetos.

### **Sintomas y Consecuencias:**

* Clase única con una gran cantidad de atributos, operaciones o ambos. Una clase con 60 o más atributos y operaciones generalmente indica la presencia del Blob

* Una colección dispar de operaciones y atributos no relacionados encapsulados en una sola clase. Una falta general de cohesión de los atributos y operaciones es típica de Blob.

* Una sola clase de controlador con clases de objetos de datos simples asociadas.

* Ausencia de diseño orientado a objetos. Un bucle principal del programa dentro de la clase Blob asociado con objetos de datos relativamente pasivos. La clase de controlador único a menudo encapsula casi toda la funcionalidad de la aplicación, al igual que un programa principal de procedimiento.

* Un diseño heredado migrado que no se ha refactorizado correctamente en una arquitectura orientada a objetos.

* El Blob compromete las ventajas inherentes de un diseño orientado a objetos. Por ejemplo, The Blob limita la capacidad de modificar el sistema sin afectar la funcionalidad de otros objetos encapsulados. Las modificaciones al Blob afectan el software extenso dentro de la encapsulación del Blob. También es probable que las modificaciones en otros objetos del sistema tengan un impacto en el software de Blob.

* La clase Blob suele ser demasiado compleja para su reutilización y prueba. Puede ser ineficaz o introducir una complejidad excesiva reutilizar el Blob para subconjuntos de su funcionalidad.

* La clase Blob puede ser costosa de cargar en la memoria, ya que usa recursos excesivos, incluso para operaciones simples.

### **Causas:**

* Falta de una arquitectura orientada a objetos. Es posible que los diseñadores no tengan una comprensión adecuada de los principios orientados a objetos. Alternativamente, el equipo puede carecer de las habilidades de abstracción adecuadas.

* Falta de (alguna) arquitectura. La ausencia de definición de los componentes del sistema, sus interacciones y el uso específico de los lenguajes de programación seleccionados. Esto permite que los programas evolucionen de manera ad hoc porque los lenguajes de programación se utilizan para fines distintos a los previstos.

* Falta de aplicación de la arquitectura. A veces, este AntiPattern crece accidentalmente, incluso después de que se planeó una arquitectura razonable. Esto puede ser el resultado de una revisión arquitectónica inadecuada a medida que se lleva a cabo el desarrollo. Esto es especialmente frecuente en los equipos de desarrollo nuevos en la orientación a objetos.

* Intervención demasiado limitada. En proyectos iterativos, los desarrolladores tienden a agregar pequeñas piezas de funcionalidad a las clases trabajadoras existentes, en lugar de agregar nuevas clases o revisar la jerarquía de clases para una asignación de responsabilidades más efectiva.

* Desastre especificado. A veces, el Blob resulta de la forma en que se especifican los requisitos. Si los requisitos dictan una solución de procedimiento, entonces se pueden realizar compromisos de arquitectura durante el análisis de requisitos que son difíciles de cambiar. Definir la arquitectura del sistema como parte del análisis de requisitos suele ser inapropiado y, a menudo, conduce al Blob AntiPattern, o algo peor.

### **Refactored Solution:**

Como ocurre con la mayoría de los AntiPatterns de esta sección, la solución implica una forma de refactorización. La clave es alejar el comportamiento del Blob. Puede ser apropiado reasignar el comportamiento a algunos de los objetos de datos encapsulados de manera que estos objetos sean más capaces y el Blob menos complejo. El método para refactorizar las responsabilidades se describe a continuación:

1. Identificar o categorizar atributos y operaciones relacionados de acuerdo con los contratos. Estos contratos deben ser cohesivos en el sentido de que todos se relacionan directamente con un enfoque, comportamiento o función común dentro del sistema general. Por ejemplo, un diagrama de arquitectura de un sistema de biblioteca se representa con una clase Blob potencial llamada LIBRARY.
En el ejemplo que se muestra en la figura 1, la clase LIBRARY encapsula la suma total de todas las funciones del sistema. Por lo tanto, el primer paso es identificar conjuntos cohesivos de operaciones y atributos que representan contratos. En este caso, podríamos recopilar operaciones relacionadas con la gestión de catálogos, como Sort_Catalog y Search_Catalog.

También podríamos identificar todas las operaciones y atributos relacionados con elementos individuales, como Print_Item, Delete_Item, etc.

![figura1]()

![figura2]()

2. El segundo paso es buscar "hogares naturales" para estas colecciones de funcionalidad basadas en contratos y luego migrarlas allí. En este ejemplo, recopilamos operaciones relacionadas con catálogos y las migramos de la clase LIBRARY y las trasladamos a la clase CATALOG.

Hacemos lo mismo con las operaciones y atributos relacionados con los artículos, moviéndolos a la clase ITEM. Esto simplifica la clase LIBRARY y hace que las clases ITEM y CATALOG sean más que simples tablas de datos encapsulados. El resultado es un mejor diseño orientado a objetos.

![figura3]()

3. El tercer paso es eliminar todas las asociaciones indirectas "acopladas a distancia" o redundantes. En el ejemplo, la clase ITEM está inicialmente acoplada de forma remota a la clase LIBRARY en que cada elemento realmente pertenece a un CATALOG, que a su vez pertenece a una LIBRARY.

4. A continuación, cuando sea apropiado, migramos asociados a clases derivadas a una clase base común. En el ejemplo, una vez que se ha eliminado el acoplamiento lejano entre las clases LIBRARY y ITEM, debemos migrar los ITEM a los CATALOG, como se muestra en la figura 4.

![figura4]()

5. Finalmente, eliminamos todas las asociaciones transitorias, reemplazándolas según corresponda con especificadores de tipo para atributos y argumentos de operaciones.

En nuestro ejemplo, un Check_Out_Item o un Search_For_Item sería un proceso transitorio y se podría mover a una clase transitoria separada con atributos locales que establecen la ubicación específica o los criterios de búsqueda para una instancia específica de un check-out o búsqueda.

### **Ejemplo:**

Un módulo GUI que está destinado a interactuar con un módulo de procesamiento adquiere gradualmente la funcionalidad de procesamiento de los módulos de procesamiento en segundo plano. Un ejemplo de esto es una pantalla de PowerBuilder para la entrada / recuperación de datos del cliente. La pantalla puede:

1. Mostrar datos.
2. Editar datos.
3. Realice una validación de tipo simple. Luego, el desarrollador agrega funcionalidad a lo que estaba destinado a ser el motor de decisiones:
    3.1. Validación compleja.
    3.2. Algoritmos que utilizan los datos validados para evaluar las próximas acciones.

4. Luego, el desarrollador obtiene nuevos requisitos para:
    4.1. Extienda la GUI a tres formas.
    4.2. Hágalo basado en secuencias de comandos (incluido el desarrollo de un motor de secuencias de comandos).
    4.3. Agregue nuevos algoritmos al motor de decisiones.

El desarrollador amplía el módulo actual para incorporar todas estas funciones. Entonces, en lugar de desarrollar varios módulos, se desarrolla un solo módulo. Si la aplicación prevista está diseñada y diseñada, es más fácil de mantener y ampliar.


[Referencas](https://sourcemaking.com/antipatterns/the-blob)