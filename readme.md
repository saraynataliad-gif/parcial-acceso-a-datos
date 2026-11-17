# Sistema de Inventario de Zapatos — SQLAlchemy ORM

## 1. Información del proyecto

| Información | Descripción |
|---|---|
| Estudiante | [Saray Natalia Duarte Florez] |
| Asignatura | [Acceso a Datos] |
| Docente | [Eduardo Pimienta] |
| Fecha | [17/11/2026] |
| Lenguaje de programación | Python |
| ORM utilizado | SQLAlchemy |
| Base de datos | SQLite |

## 2. Descripción del proyecto

**¿En qué consiste el programa?**

[Este proyecto es una aplicación de consola en Python creada para llevar el control de inventario de una tienda de zapatos. Básicamente, su función principal es conectar nuestro código con una base de datos local en SQLite utilizando SQLAlchemy como un ORM. Administra información esencial de los productos como su identificador único (id), el modelo, la talla y el precio y su propósito principal en este parcial es demostrar que podemos hacer todas las operaciones CRUD (crear, listar, buscar, actualizar y eliminar) manejando objetos de Python, asegurando que los datos se queden guardados de forma permanente en el equipo sin necesidad de escribir sentencias SQL manuales.]

**¿Qué funcionalidades tiene?**

Describe brevemente las operaciones que permite realizar el sistema:

-Registrar zapatos: Permite dar de alta nuevos productos en la base de datos escribiendo por consola el modelo, la talla y el precio del zapato.
-Consultar el inventario: Muestra en pantalla una lista completa con todos los zapatos que tenemos guardados hasta el momento.
-Buscar zapatos por ID: Sirve para localizar un artículo en concreto ingresando su número de identificación único, facilitando encontrar un producto específico.
-Actualizar precios: Permite modificar el costo de cualquier zapato ya registrado cuando sea necesario, actualizando la información de inmediato.
-Eliminar zapatos: Da la opción de borrar por completo un registro de la base de datos utilizando su ID si el producto ya no está disponible

## 3. Estructura del proyecto

Presenta la estructura de archivos de tu aplicación.

```text
tienda_zapatos/
├── main.py
├── datos.py
├── requirements.txt
├── README.md
└── evidencias/
```

**Explicación de los archivos:**

| Archivo | ¿Cuál es su responsabilidad? |
|---|---|
| main.py | Controla el flujo principal del programa, mostrando el menú interactivo por consola y gestionando las opciones elegidas por el usuario. |
| datos.py | Contiene la configuración del ORM de SQLAlchemy, el modelo de la tabla y todas las funciones del CRUD para interactuar con la base de datos. |
| requirements.txt | Almacena las dependencias y librerías externas necesarias (como SQLAlchemy) para que el proyecto pueda ejecutarse sin problemas. |
| zapatos.db | Es el archivo de la base de datos SQLite donde se almacena de forma persistente toda la información de los zapatos. Se genera automáticamente la primera vez que se ejecuta el programa al inicializar el ORM. |

## 4. Instalación y ejecución

Explica los pasos para ejecutar el proyecto en otro computador.

**Paso 1. Requisitos**

[Indica los programas y herramientas necesarios.]

Tener instalado Python en el equipo (versión reciente)

**Paso 2. Instalación de dependencias**

```bash
python -m pip install -r requirements.txt
```
Un editor de código o terminal (como Visual Studio Code y la consola de comandos)

**Paso 3. Ejecución**

```bash
python main.py
```
Conexión a internet únicamente la primera vez para instalar la librería mediante pip

**Paso 4. Resultado esperado**

[Describe qué aparece cuando se ejecuta correctamente la aplicación.]

---

Al ejecutar el comando correctamente, la terminal abre de inmediato el menú interactivo de la tienda de zapatos con sus opciones numeradas del 1 al 6, permitiendo interactuar con el sistema de inventario y verificar que la base de datos responde de manera adecuada

# 5. Documentación técnica — Preguntas obligatorias

Responde las siguientes preguntas utilizando tu implementación. Cuando sea necesario, incluye fragmentos de tu código para explicar el funcionamiento.

### Pregunta 1. Modelo y tabla

¿Qué clase de Python representa la tabla de la base de datos? Explica cómo SQLAlchemy identifica el nombre de la tabla y sus columnas.

**Respuesta:**

[La clase de Python encargada de representar la tabla es Zapato. SQLAlchemy sabe exactamente a qué tabla de la base de datos corresponde gracias al atributo _tablename_ = 'zapatos' que definimos dentro de la clase. Por su parte, las columnas se identifican y mapean utilizando objetos de tipo Column, donde especificamos su tipo de dato en Python (Integer, String, Float) y sus propiedades especiales, como por ejemplo que id sea la llave primaria (primary_key=True) y autoincrementable.]

**Fragmento de código relacionado:**

[class Zapato(Base):
    __tablename__ = 'zapatos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    modelo = Column(String, nullable=False)
    talla = Column(Integer, nullable=False)
    precio = Column(Float, nullable=False)

    Aquí definimos la clase Zapato que hereda de Base. Con _tablename_ = 'zapatos' le indicamos a SQLAlchemy cómo debe llamarse la tabla en SQLite, y mediante la clase Column configuramos cada uno de los campos con sus respectivos tipos de datos y restricciones clave]



### Pregunta 2. Creación de la base de datos

¿Qué ocurre cuando ejecutas el programa por primera vez? Explica cómo se crea la base de datos `zapateria.db` y la tabla `zapatos`.

**Respuesta:**

[Cuando ejecutamos el programa por primera vez, create_engine detecta que el archivo aún no existe y crea localmente el archivo SQLite (zapatos.db). Luego, la función inicializar_bd() ejecuta Base.metadata.create_all(engine), la cual lee todas las clases que heredan de Base (en este caso, nuestro modelo Zapato) y construye automáticamente la estructura física de la tabla dentro de la base de datos.]

**Fragmento de código relacionado:**

[engine = create_engine("sqlite:///zapatos.db", echo=False)

def inicializar_bd():
    Base.metadata.create_all(engine).

    En este bloque creamos el motor de conexión (engine) apuntando al archivo local zapatos.db. La función inicializar_bd() utiliza Base.metadata.create_all(engine) para leer el modelo que mapeamos y construir físicamente la tabla en la base de datos la primera vez que se ejecuta]

### Pregunta 3. Registro de zapatos

Cuando seleccionas la opción de registrar un zapato, ¿qué recorrido siguen los datos desde el menú hasta quedar almacenados en SQLite? Identifica las funciones utilizadas.

**Respuesta:**

El recorrido comienza cuando el usuario interactúa con el menú principal en main.py y digita los datos solicitados. Esos valores se pasan como parámetros a la función crear_zapato(modelo, talla, precio) ubicada en datos.py. Dentro de esta función se crea una instancia del modelo Zapato, se añade a la sesión activa mediante session.add() y se confirma con session.commit(), lo que genera de forma automática la instrucción SQL INSERT que guarda la información en SQLite

**Fragmento de código relacionado:**

[def crear_zapato(modelo, talla, precio):
    session = Session()
    nuevo_zapato = Zapato(modelo=modelo, talla=talla, precio=precio)
    session.add(nuevo_zapato)
    session.commit()
    session.close().

Esta función abre una sesión de trabajo con Session(), instancia un nuevo objeto de la clase Zapato con los datos ingresados por el usuario, lo añade a la sesión con session.add() y confirma la transacción de forma permanente usando session.commit(), lo que genera el INSERT en SQLite]

### Pregunta 4. Sesiones y transacciones

¿Para qué se utiliza una sesión de SQLAlchemy? ¿Qué ocurriría si agregas o modificas un objeto, pero no confirmas la transacción con `commit()`?

**Respuesta:**

[Una sesión (Session) actúa como un espacio de trabajo temporal que gestiona las consultas y transacciones con la base de datos. Si agregamos o modificamos un registro pero omitimos el session.commit(), los cambios se quedan congelados en la memoria de la sesión y nunca llegan a escribirse de manera permanente en el archivo de la base de datos.]

### Pregunta 5. Búsqueda por ID

¿Cómo funciona la búsqueda de zapatos por ID? Explica qué devuelve tu función cuando encuentra el registro y qué devuelve cuando no existe.

**Respuesta:**

[La función buscar_zapato(zapato_id) realiza una consulta filtrando directamente por la llave primaria con la instrucción session.query(Zapato).filter_by(id=zapato_id).first(). Si el registro con ese ID existe en la base de datos, la función retorna la instancia completa del objeto Zapato; de lo contrario, si no encuentra coincidencia, devuelve None.]

**Fragmento de código relacionado:**

[def buscar_zapato(zapato_id):
    session = Session()
    zapato = session.query(Zapato).filter_by(id=zapato_id).first()
    session.close()
    return zapato.
    
    Aquí utilizamos el método filter_by(id=zapato_id) junto con .first() para realizar una consulta filtrada directamente por la llave primaria. Si el registro existe nos devuelve el objeto completo, y si no, retorna None]

### Pregunta 6. Actualización de precios

¿Cómo se actualiza el precio de un zapato mediante el ORM? Explica cómo se obtiene el objeto, cómo se modifica su atributo y cómo se guarda el cambio.

**Respuesta:**

[Primero se localiza el registro en la base de datos filtrando por su ID. Una vez obtenido el objeto en Python, modificamos directamente su atributo de precio escribiendo zapato.precio = nuevo_precio. Por último, invocamos session.commit() para que el ORM traduzca esa modificación en una sentencia UPDATE que actualice permanentemente el valor en SQLite.]

**Fragmento de código relacionado:**

[def actualizar_precio(zapato_id, nuevo_precio):
    session = Session()
    zapato = session.query(Zapato).filter_by(id=zapato_id).first()
    if zapato:
        zapato.precio = nuevo_precio
        session.commit()
    session.close().

Primero buscamos el zapato por su ID único. Una vez que lo obtenemos en una variable de Python, modificamos directamente su atributo de precio (zapato.precio = nuevo_precio) y guardamos el cambio aplicando session.commit() para que el ORM actualice el registro]

### Pregunta 7. Eliminación de registros

¿Qué ocurre cuando eliminas un zapato? Explica cómo compruebas que el registro ya no existe en la base de datos.

**Respuesta:**

[La función busca el registro por su ID y, al encontrarlo, ejecuta session.delete(zapato) seguido de session.commit(). Podemos comprobar que el registro fue borrado con éxito intentando buscarlo nuevamente (lo cual arrojará None) o consultando el listado general del inventario para verificar visualmente que ya no aparece.]

**Fragmento de código relacionado:**

[def eliminar_zapato(zapato_id):
    session = Session()
    zapato = session.query(Zapato).filter_by(id=zapato_id).first()
    if zapato:
        session.delete(zapato)
        session.commit()
    session.close().

En esta función localizamos el registro por su ID y, si lo encontramos, ejecutamos session.delete(zapato) seguido de session.commit(). Esto borra el artículo de la base de datos de manera definitiva]

### Pregunta 8. Persistencia de datos

¿Qué sucede con los zapatos registrados cuando cierras y vuelves a ejecutar el programa? Explica por qué permanecen almacenados.

**Respuesta:**

[Los zapatos no se borran y se conservan intactos. Esto ocurre porque la información no se almacena en la memoria volátil de la ejecución, sino que se guarda directamente en un archivo físico de SQLite (zapatos.db) en el disco de la computadora, garantizando una persistencia real de los datos al cerrar la aplicación.]

---

## 6. Pruebas de funcionamiento y evidencias

Debes ejecutar el programa y demostrar el funcionamiento de cada una de las operaciones.

### Prueba 1. Registrar zapatos

- **Acción realizada:** registrar dos zapatos.
- **Datos utilizados:** [: Modelo: clasico, Talla: 38, Precio: 150000; y Modelo: colegial, Talla: 40, Precio: 150000].
- **Resultado obtenido:** [El sistema procesó la información y mostró en la consola el mensaje de éxito indicando que cada zapato se registró correctamente en la base de datos].

**Evidencia:**

![Registro de zapatos](evidencias/prueba1.png)

### Prueba 2. Listar inventario

- **Acción realizada:** consultar todos los zapatos.
- **Resultado obtenido:** [El programa desplegó una lista completa en pantalla mostrando los detalles (ID, modelo, talla y precio) de todos los artículos guardados.]

**Evidencia:**

![Listado de zapatos](evidencias/prueba2.png)

### Prueba 3. Buscar por ID

- **ID utilizado:** [2].
- **Resultado obtenido:** [El sistema consultó la base de datos y encontró el zapato exacto con ese identificador, mostrando su información detallada en la consola.].

**Evidencia:**

![Búsqueda de zapatos](evidencias/prueba3.png)

### Prueba 4. Actualizar precio

- **Zapato seleccionado:** [ID:2].
- **Precio anterior:** [150000].
- **Precio nuevo:** [180000].
- **Resultado obtenido:** [El ORM localizó el registro, modificó su precio y aplicó los cambios de forma permanente, confirmando la actualización con un mensaje en pantalla.].

**Evidencia:**

![Actualización de precio](evidencias/prueba4.png)

### Prueba 5. Eliminar zapato

- **ID eliminado:** [2].
- **Resultado obtenido:** [El sistema borró el registro de la base de datos utilizando su ID. Lo verifiqué volviendo a listar el inventario y comprobando visualmente que el zapato ya no aparecía.].

**Evidencia:**

![Eliminación de zapato](evidencias/prueba5.png)

### Prueba 6. Comprobar persistencia

- **Acción realizada:** cerrar y ejecutar nuevamente el programa.
- **Resultado obtenido:** [Los registros que guardamos previamente permanecieron intactos y almacenados, demostrando que la información se guardó de forma física en el archivo SQLite].

**Evidencia:**

![Persistencia de datos](evidencias/prueba6.png)

### Pruebas con registros inexistentes

Ejecuta las operaciones de buscar, actualizar y eliminar utilizando un ID que no exista.

| Operación | ¿Qué sucedió? |
|---|---|
| Buscar ID inexistente | El programa indicó de manera controlada que no se encontró ningún zapato con ese ID y retornó un valor vacío (None) sin generar caídas en el sistema. |
| Actualizar ID inexistente | El sistema informó que el ID no existía en la base de datos y no aplicó ninguna modificación. |
| Eliminar ID inexistente | La consola mostró un mensaje advirtiendo que no se encontró ningún registro con ese ID para eliminar. |

## 7. Conclusiones

Responde brevemente:

1. ¿Qué aprendiste al implementar las operaciones CRUD utilizando SQLAlchemy?

Aprendi a utilizar un ORM, como SQLAlchemy en Python para gestionar bases de datos relacionales sin necesidad de escribir sentencias SQL manuales, Comprendi como se mapean las clases a tablas mediante modelos y la importancia de administrar las sesiones y las transacciones para garantizar la persistencia segura de los datos

2. ¿Qué diferencia identificaste entre trabajar con objetos Python y escribir sentencias SQL directamente?

La principal diferencia es la abstraccion y la orientacion a objetos. Al trabajar con SQLAlchemy, manipulamos instancias de clases de Python (como crear o modificar un objeto y cambiar sus atributos directamente) en lugar de redactar consultas de texto plano con sintaxis SQL (INSERT, SELECT, UPDATE, DELETE). Esto hace que el codigo sea mas limpio, mantenible y menos propenso a errores de sintaxis en las tablas

3. ¿Cuál fue la principal dificultad durante el desarrollo y cómo la solucionaste?

La principal dificultad estuvo relacionada con las restricciones del entorno de la sala de sistemas y la adaptación de los nombres de funciones preestablecidos en el archivo principal, Se solucionó configurando adecuadamente las dependencias locales y ajustando los nombres de las funciones en el modulo de datos para que coincidieran exactamente con lo que el programa principal requería al inicializar la base de datos y ejecutar el CRUD


## Indicaciones de documentación

- Responde las ocho preguntas con tus propias palabras.
- Relaciona tus explicaciones con el código que implementaste.
- Incluye fragmentos de código únicamente cuando ayuden a explicar tu respuesta.
- Todas las evidencias deben corresponder a ejecuciones reales del programa.
- Guarda las capturas dentro de la carpeta `evidencias/` utilizando los nombres indicados o actualiza las rutas del README.
- Verifica que las imágenes se visualicen correctamente en GitHub.
- Elimina los textos entre corchetes y reemplázalos con tus respuestas antes de entregar.
- La documentación debe permitir que otra persona comprenda cómo instalar, ejecutar y utilizar tu aplicación.