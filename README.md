# Desarrollo de APIs con Python — Clase 4

Este repositorio contiene el estado final del proyecto correspondiente a la **Clase 4** de la asignatura **Desarrollo de APIs con Python**.

Su propósito es servir como referencia para que los estudiantes puedan comparar el resultado obtenido después de trabajar sobre el proyecto de la **Clase 3** y reproducir en casa los pasos desarrollados durante esta sesión.

---

## Punto de partida

La Clase 4 parte del estado final alcanzado en la Clase 3.

En ese punto el proyecto ya dispone de:

- una aplicación FastAPI funcional;
- modelos Pydantic de entrada y salida;
- validaciones de datos;
- `APIRouter`;
- separación inicial entre routers y schemas;
- path parameters;
- query parameters;
- dependencias básicas con `Depends`;
- manejo inicial de errores mediante `HTTPException`;
- documentación automática mediante OpenAPI y Swagger UI.

Durante esta clase el proyecto evoluciona para incorporar una separación inicial de responsabilidades y comenzar a trabajar con **desarrollo guiado por especificaciones (SDD)**.

---

## Objetivos de la Clase 4

En esta clase se trabajan los siguientes objetivos:

- reorganizar una API usando routers, schemas, servicios y configuración;
- reconocer responsabilidades iniciales dentro del proyecto;
- transformar una necesidad en requerimientos;
- diferenciar requerimientos funcionales y no funcionales;
- escribir criterios de aceptación verificables;
- utilizar Given / When / Then para expresar comportamientos esperados;
- crear una primera especificación antes de modificar código;
- comprender la relación entre especificación, plan y tareas;
- introducir una estructura básica de gobernanza para el trabajo con SDD;
- utilizar plantillas para mantener consistencia entre especificaciones;
- introducir el uso de un LLM como apoyo para redactar y revisar artefactos de desarrollo.

---

## Estructura esperada del proyecto

Al finalizar la clase, la estructura del proyecto será similar a:

```text
.
├── AGENTS.md
│
├── app/
│   ├── main.py
│   ├── config.py
│   ├── routers/
│   │   ├── __init__.py
│   │   └── projects.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── projects.py
│   └── services/
│       ├── __init__.py
│       └── projects.py
│
├── specs/
│   ├── constitution.md
│   │
│   ├── templates/
│   │   ├── spec-template.md
│   │   ├── plan-template.md
│   │   └── tasks-template.md
│   │
│   └── 001-create-project/
│       ├── spec.md
│       ├── plan.md
│       └── tasks.md
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Requisitos

Para ejecutar este proyecto se necesita:

- Git
- Docker Desktop o Docker Engine con Docker Compose

No es necesario instalar Python ni las dependencias del proyecto directamente en el sistema operativo.

Docker se encargará de construir el entorno de ejecución.

---

## Clonar el repositorio

Ejecute:

```bash
git clone <URL_DEL_REPOSITORIO>
```

Luego entre en la carpeta:

```bash
cd desarrollo_api-python-clase04
```

---

## Construir y ejecutar la aplicación

La primera vez que ejecute el proyecto, Docker deberá construir la imagen e instalar las dependencias definidas en `requirements.txt`.

Ejecute:

```bash
docker compose up --build
```

Cuando la aplicación haya iniciado correctamente, debería aparecer un mensaje similar a:

```text
Uvicorn running on http://0.0.0.0:8000
```

---

## Abrir la documentación de la API

Desde el navegador abra:

```text
http://localhost:8000/docs
```

FastAPI mostrará automáticamente la documentación interactiva de la API mediante Swagger UI.

También puede consultar la especificación OpenAPI en:

```text
http://localhost:8000/openapi.json
```

---

# Modularidad y separación de responsabilidades

Uno de los principales objetivos de esta clase es evitar que toda la lógica de la aplicación permanezca concentrada dentro de los routers.

La separación inicial utilizada es:

```text
main.py
→ crea y ensambla la aplicación

routers/
→ define la frontera HTTP

schemas/
→ define los contratos de entrada y salida

services/
→ representa operaciones de aplicación

config.py
→ centraliza valores de configuración
```

Esta estructura no pretende representar todavía la arquitectura final del curso.

La idea es introducir separaciones únicamente cuando existe una responsabilidad claramente diferenciada.

---

## Router como frontera HTTP

Los routers deben concentrarse principalmente en aspectos relacionados con HTTP:

```text
path
method
request model
response model
status code
HTTP error mapping
```

El router no debería convertirse en el lugar donde vive toda la lógica de la aplicación.

Una pregunta útil para revisar el código es:

```text
¿Esta línea pertenece al contrato HTTP
o a la operación que quiero ejecutar?
```

---

## Servicios

Durante esta clase se introduce una carpeta:

```text
app/services/
```

Un servicio inicial puede ser simplemente una función.

No es necesario utilizar clases si una función expresa adecuadamente la intención de la operación.

Por ejemplo:

```python
def create_project(
    name: str,
    description: str | None,
) -> ProjectResponse:
    ...
```

El objetivo es que el router delegue la operación y mantenga una responsabilidad más clara.

---

## Configuración

También se introduce:

```text
app/config.py
```

para evitar que determinados valores permanezcan dispersos en diferentes archivos.

Ejemplos de valores que pueden formar parte de la configuración:

```text
application title
environment name
debug mode
database URL
token expiration
```

En esta clase se utiliza una configuración sencilla.

Más adelante se incorporarán variables de entorno, archivos `.env` y manejo de secretos.

---

## No sobrearquitectura

En este punto del curso todavía no es necesario introducir:

```text
Domain
Repository
Unit of Work
Hexagonal Architecture
```

La regla utilizada durante esta etapa es:

```text
problema visible
→ separación justificada
```

No se agregan patrones únicamente para hacer que el proyecto parezca más complejo o profesional.

---

# Desarrollo guiado por especificaciones

A partir de esta clase se introduce **SDD — Specification-Driven Development**.

La idea principal es reducir una práctica común:

```text
abrir el editor
→ comenzar a escribir código
→ decidir después qué debía hacer
```

El nuevo flujo busca comenzar por aclarar la intención.

---

## Flujo básico de SDD

El flujo trabajado en esta clase es:

```text
Necesidad
→ Requerimiento
→ Especificación
→ Plan
→ Tareas
→ Implementación
→ Verificación
```

Cada etapa responde una pregunta distinta.

---

# Gobernanza inicial del proyecto

Además de crear especificaciones concretas, el proyecto incorpora una estructura mínima de gobernanza.

El objetivo es que las especificaciones no dependan únicamente de decisiones improvisadas durante cada cambio.

La estructura utilizada es:

```text
AGENTS.md
→ reglas generales de trabajo del repositorio

specs/constitution.md
→ principios que deben respetar las especificaciones y cambios

specs/templates/
→ formatos reutilizables para spec, plan y tasks

specs/001-create-project/
→ aplicación concreta de esas reglas
```

Estos archivos se incorporan desde esta etapa para familiarizar al estudiante con una forma de trabajo reproducible.

En clases posteriores también podrán ser utilizados como contexto por herramientas de inteligencia artificial y agentes de desarrollo.

---

## `AGENTS.md`

`AGENTS.md` contiene instrucciones generales para trabajar dentro del repositorio.

Puede definir aspectos como:

- estructura esperada del proyecto;
- reglas para modificar código;
- uso de especificaciones;
- alcance de los cambios;
- obligación de verificar antes de aceptar una modificación;
- archivos que no deberían modificarse sin justificación.

Aunque todavía no se utilicen agentes de desarrollo durante toda la práctica, este archivo prepara el repositorio para ese tipo de herramientas.

También sirve como documentación de trabajo para desarrolladores humanos.

---

## `constitution.md`

El archivo:

```text
specs/constitution.md
```

define principios generales que deben mantenerse durante el desarrollo.

Ejemplos:

```text
Los cambios deben partir de una necesidad identificada.

Los requerimientos deben ser verificables.

No deben inventarse requisitos fuera del alcance acordado.

El código debe modificarse únicamente después de revisar la especificación.

Los cambios deben ser pequeños y observables.

La implementación debe poder relacionarse con requerimientos y criterios de aceptación.
```

La constitución no describe una funcionalidad específica.

Describe reglas que deberían mantenerse entre diferentes funcionalidades.

---

# Plantillas SDD

La carpeta:

```text
specs/templates/
```

contiene formatos reutilizables para evitar que cada nueva especificación tenga una estructura diferente.

---

## `spec-template.md`

La plantilla de especificación puede contener secciones como:

```text
Feature
Need
Scope
Functional Requirements
Non-Functional Requirements
Acceptance Criteria
Out of Scope
```

Cada feature concreta utilizará esta estructura como punto de partida.

---

## `plan-template.md`

La plantilla de planificación permite organizar la estrategia antes de editar código.

Puede incluir:

```text
Current State
Files Involved
Implementation Strategy
Verification Strategy
Risks
```

El plan no contiene todavía la implementación.

Describe cómo se pretende realizarla.

---

## `tasks-template.md`

La plantilla de tareas transforma el plan en unidades pequeñas y observables.

Las tareas deberían:

- ser concretas;
- tener un alcance reducido;
- poder marcarse como completadas;
- relacionarse con el plan;
- evitar modificaciones no justificadas.

---

## Necesidad

Una necesidad describe el problema o el valor buscado desde el punto de vista del uso.

Ejemplo:

```text
Users need to create projects so they can organize work.
```

Una necesidad no debería comenzar describiendo directamente una implementación.

Por ejemplo:

```text
Create a table called projects.
```

no representa una necesidad, sino una posible decisión técnica.

---

## Requerimientos funcionales

Los requerimientos funcionales describen comportamientos que el sistema debe ofrecer.

Ejemplos:

```text
FR-001
The system shall allow creating a project.

FR-002
The system shall allow listing projects.

FR-003
The system shall reject invalid project names.
```

Los requerimientos deben ser:

```text
claros
trazables
verificables
```

---

## Requerimientos no funcionales

Los requerimientos no funcionales describen restricciones o atributos de calidad.

Ejemplos:

```text
NFR-001
The API shall expose OpenAPI documentation.

NFR-002
The project shall run locally using Docker Compose.

NFR-003
The repository shall not track `.env` files.
```

Los requerimientos no funcionales no son menos importantes.

Representan otro tipo de condición que también debe poder verificarse.

---

# Primera especificación

Durante esta clase se crea:

```text
specs/
└── 001-create-project/
    ├── spec.md
    ├── plan.md
    └── tasks.md
```

Estos archivos representan una instancia concreta del proceso definido por la gobernanza y las plantillas.

El objetivo no es introducir burocracia.

La finalidad es conservar de forma explícita la intención del cambio antes de modificar el código.

---

## `spec.md`

`spec.md` describe principalmente:

- la necesidad;
- el alcance;
- los requerimientos funcionales;
- los requerimientos no funcionales cuando corresponda;
- los criterios de aceptación;
- aquello que queda fuera del alcance.

Ejemplo conceptual:

```markdown
# Feature: Create Project

## Need

Users need to create projects to organize work.

## Functional Requirements

FR-001: The system shall allow creating a project
with a name and optional description.

FR-002: The system shall reject project names
shorter than 3 characters.
```

---

## Criterios de aceptación

Un criterio de aceptación transforma un requerimiento en una condición verificable.

Ejemplo:

```text
AC-001

Given a valid project name
When the user creates a project
Then the API returns 201
And the response includes the project name.
```

El objetivo es que este comportamiento pueda convertirse posteriormente en una prueba automatizada.

---

## Given / When / Then

La estructura utilizada es:

```text
Given
→ estado o contexto inicial

When
→ acción ejecutada

Then
→ resultado esperado

And
→ condiciones adicionales
```

Esta forma ayuda a reducir ambigüedades y hace más explícito el comportamiento esperado.

---

## Ejemplo de criterio para entrada inválida

```text
AC-002

Given a project name shorter than 3 characters
When the user attempts to create a project
Then the API returns 422
And no project is accepted.
```

Este criterio deberá poder verificarse posteriormente mediante una prueba.

---

## `plan.md`

`plan.md` describe la estrategia que se seguirá antes de modificar código.

Ejemplo:

```markdown
# Implementation Plan

1. Review current project creation endpoint.
2. Confirm request and response schemas.
3. Add acceptance criteria to `spec.md`.
4. Add validation to `ProjectCreate`.
5. Verify behavior in `/docs`.
```

El plan no es código.

Es una guía para controlar cómo se realizará el cambio.

---

## `tasks.md`

`tasks.md` transforma el plan en trabajo pequeño y observable.

Ejemplo:

```markdown
# Tasks

- [ ] T-001 Create feature folder.
- [ ] T-002 Write functional requirements.
- [ ] T-003 Write acceptance criteria.
- [ ] T-004 Update schema validation.
- [ ] T-005 Verify behavior manually.
```

Las tareas deben ser lo suficientemente pequeñas como para poder comprobar si fueron realizadas.

---

# Uso de inteligencia artificial

Durante esta clase se introduce el uso de un **LLM como apoyo al proceso de desarrollo**.

Todavía no se delega el desarrollo completo a un agente.

El modelo puede ayudar a:

```text
analizar ambigüedades
redactar requerimientos
proponer criterios de aceptación
generar spec.md
generar plan.md
generar tasks.md
```

Sin embargo, la responsabilidad técnica continúa siendo del estudiante.

El estudiante debe:

- definir o aclarar la necesidad;
- revisar los requerimientos generados;
- detectar supuestos no autorizados;
- comprobar los criterios de aceptación;
- verificar que el plan respete la especificación;
- comprobar que las tareas no introduzcan trabajo fuera del alcance.

La IA puede proponer contenido.

El desarrollador decide si ese contenido es aceptado.

---

## Detectar ambigüedades antes de generar

Antes de pedir al LLM que genere una especificación, se recomienda solicitar primero un análisis.

Ejemplo:

```text
Analyze the following need and current project context.

Do not create the specification yet.

Identify:
1. ambiguities;
2. missing information;
3. assumptions that should not be made;
4. questions that should be answered before implementation.
```

Después de resolver esas dudas se puede solicitar:

```text
Create spec.md, plan.md and tasks.md
using only the clarified requirements.

Follow the project constitution and templates.

Do not invent requirements outside the defined scope.
```

---

## Responsabilidad del desarrollador

El uso de IA no elimina la responsabilidad del estudiante.

La secuencia esperada es:

```text
desarrollador define necesidad
        ↓
reglas de gobernanza delimitan el trabajo
        ↓
LLM analiza ambigüedades
        ↓
desarrollador aclara
        ↓
LLM propone artefactos
        ↓
desarrollador revisa
        ↓
se aceptan o corrigen
        ↓
recién después se modifica código
```

No se considera correcta una especificación únicamente porque fue producida por un modelo.

---

## Verificación manual

Antes de introducir pruebas automatizadas completas, algunos criterios pueden verificarse manualmente.

Ejemplos:

```text
AC-001
→ probar payload válido en `/docs`

AC-002
→ probar payload inválido en `/docs`

NFR-001
→ abrir `/openapi.json`

NFR-002
→ levantar el proyecto con `docker compose up`
```

En clases posteriores estas verificaciones comenzarán a formalizarse mediante pruebas automatizadas.

---

## Detener la aplicación

Si Docker Compose está ejecutándose en primer plano:

```text
Ctrl+C
```

Luego:

```bash
docker compose down
```

---

## Reconstruir la imagen

Si se modifica `Dockerfile` o `requirements.txt`, puede reconstruir la imagen con:

```bash
docker compose up --build
```

Para cambios normales en archivos Python no debería ser necesario reconstruir la imagen si el proyecto está montado como volumen y Uvicorn utiliza recarga automática.

---

# Propósito de este repositorio

Este repositorio representa el **estado final esperado de la Clase 4**.

El estudiante puede utilizar el repositorio de la Clase 3 como punto de partida y reproducir paso a paso los cambios desarrollados durante esta sesión.

Después puede utilizar este repositorio para comparar:

```text
estado inicial
→ cambios realizados
→ estado final esperado
```

La intención no es simplemente descargar una solución terminada.

El objetivo es reconstruir y comprender el proceso que llevó hasta ella.

---

# Metodología de trabajo

A partir de esta clase el curso comienza a incorporar progresivamente una forma de trabajo guiada por intención, especificación y gobernanza.

El flujo buscado es:

```text
reglas de trabajo
→ entender el problema
→ aclarar la necesidad
→ definir requerimientos
→ especificar
→ planificar
→ dividir en tareas
→ implementar
→ verificar
```

La incorporación de inteligencia artificial no reemplaza este proceso.

La IA se utilizará como una herramienta para apoyar el razonamiento, la documentación y, posteriormente, la implementación.

---

## Lo que viene después

Las próximas etapas del curso profundizarán progresivamente en:

- pruebas automatizadas;
- Pytest;
- TDD;
- persistencia;
- PostgreSQL;
- SQLModel;
- arquitectura;
- desarrollo asistido por agentes;
- uso efectivo de `AGENTS.md`;
- generación de cambios a partir de especificaciones;
- revisión de modificaciones propuestas por IA.

Los artefactos creados en esta clase servirán como base para conectar:

```text
gobernanza
→ especificación
→ pruebas
→ implementación
→ agentes
```

---

## Autor

**Prof. José Gregorio Castillo Pacheco**

Asignatura: **Desarrollo de APIs con Python**