# ANTI-PATRONES

Los antipatrones (antipatterns) son descripciones de situaciones, o
soluciones, recurrentes que producen consecuencias negativas. Un
antipatrón puede ser el resultado de una decisión equivocada sobre
cómo resolver un determinado problema, o bien, la aplicación correcta
de un patrón de diseño en el contexto equivocado. 

Los antipatrones son una iniciativa de investigación del software
que se focaliza en soluciones con efectos negativos, contrario a los
patrones de diseño. Esta documentación sobre malas prácticas ayuda a
los arquitectos y consultores de software a evitar cometer errores recurrentes. Sin este conocimiento, los antipatrones seguirán
apareciendo en los proyectos de software. 

Como  se  muestra  en  la  Figura,  patrones  y antipatrones están relacionados de tal forma que un  patrón  puede evolucionar  hasta  convertirse en una solución de antipatrón. Cuando éste es el caso,  se dice  que estamos  en presencia  de un proceso de refactoring.

![relacionpatrones]()

## Puntos de Vista

Según (Brown et al, 1998) existen tres puntos de vista, o niveles,
desde los cuales analizar los antipatrones. Ellos son:

* **Desarrollo:** describe situaciones encontradas por programadores en
la resolución de problemas de programación.
* **Arquitectura:** estos antipatrones se centran en los problemas
recurrentes relacionados a la estructura del sistema, sus
consecuencias y soluciones.
* **Administración:** Parte del trabajo de un gerente implica comunicarse
con la gente, y resolver problemas. Los antipatrones de
administración identifican los principales escenarios donde éstos
problemas pueden llegar a ser destructivos para los proyectos de
software. 

##  Un proceso para el uso de antipatrones

Tate (2002) propone un proceso de seis pasos para el estudio de
antipatrones (ver Figura):

![Imagensolantipatron]()

1. Encontrar el problema: una falla en el comportamiento, un error en el
diseño, etc.
2. Establecer un patrón de fallas: identificar en qué condiciones se da el
problema.
3. Refactorizar el código: el código que produjo el error debe ser
refactorizado y, en la medida de lo posible, la nueva solución debería
implementarse utilizando patrones de diseño.
4. Publicar la solución: éste conocimiento debe ser diseminado con el
fin de que si otros desarrolladores se encuentran con uno similar
podrán resolverlo.
5. Identificar debilidades, o posibles problemas del proceso. A menudo
las herramientas inducen el mal uso de las mismas, en otras
oportunidades son las presiones externas (por ejemplo plazos de
entrega) las que lo hacen. Es importante tener presente que el proceso debe ser realizable por seres humanos imperfectos. En muchos casos, la educación suele ser la solución.
6. Corregir el proceso: Finalmente, una vez identificado y difundido el
antipatrón, se construye una barrera entre un problema de iguales
características y el proyecto (o empresa), de manera tal que sea
posible prevenirlo. 

## Algunos Anti-Patrones

* [Golden Hammer :hammer:]()

* [Dead Code :volcano:]()

* [Spaghetti Code :spaghetti:]()

* [The Blob :zombie:]()




