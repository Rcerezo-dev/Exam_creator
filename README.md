# Exam Creator

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.35-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-412991?style=flat&logo=openai&logoColor=white)
![Status](https://img.shields.io/badge/status-in%20development-yellow?style=flat)

This tool was born out of a practical need rather than a technical exercise. At some point I decided to stop vibecoding and build something that actually solves a problem I face every week as an English teacher: creating exams and correcting writing takes time, and a lot of that time is repetitive.

The result is a small Streamlit application that uses the OpenAI API to generate level-appropriate English exams and evaluate student writing samples. It is not trying to replace teacher judgement — it is trying to handle the mechanical parts so that judgement can go where it actually matters.

---

## How it works

The app has two main features.

**Exam generation** takes a CEFR level and an optional dyslexia-friendly flag, fills in a prompt template, and returns a ready-to-use exam. The model is instructed to produce simple instructions, no oral tasks, and five questions calibrated to the selected level.

**Writing correction** takes a student's written text, evaluates it against the expected level, and returns a structured score for grammar, vocabulary, and structure, along with a short piece of feedback. The response comes back as JSON so it can be displayed cleanly in the interface.

Both features support a dyslexia adaptation flag that adjusts the prompt accordingly.

---

## Setup

Clone the repository and install dependencies:

```bash
git clone https://github.com/Rcerezo-dev/Exam_creator.git
cd Exam_creator
pip install -r requirements.txt
```

Create a `.env` file in the root with your OpenAI API key:

```
OPENAI_API_KEY=your_api_key_here
```

Run the app:

```bash
streamlit run app.py
```

---

## Project structure

```
Exam_creator/
├── app.py                  # Streamlit UI
├── config/
│   └── settings.py         # Model name and supported levels
├── core/
│   ├── prompt_builder.py   # Template loading and prompt assembly
│   └── json_parser.py      # JSON extraction and validation
├── services/
│   ├── exam_generator.py   # Exam generation logic
│   └── writing_corrector.py
├── prompts/
│   ├── exam.txt
│   └── writing.txt
└── requirements.txt
```

---

## Future improvements

The current version covers the core workflow, but there is a lot of room to grow. Some directions worth exploring:

**More task types.** Right now the app generates a generic exam. A natural next step would be letting the teacher specify what kind of tasks to include — reading comprehension, gap fills, multiple choice, writing prompts — and have the model build the exam accordingly.

**Grammar and vocabulary focus.** Being able to tell the model "focus on past simple and irregular verbs" or "use vocabulary from the topic of environment" would make the tool far more useful in real classroom contexts.

**PDF export.** The exam currently lives inside the app. Exporting it as a formatted PDF or Word document would close the gap between generation and actual classroom use.

**Multiple subjects.** The prompts are built around English, but the architecture is general enough to support other languages or subjects with minimal changes.

**Student history.** Storing past corrections with timestamps would let teachers track progress over time and identify recurring weaknesses across a group.

---

---

# Exam Creator

Esta herramienta nació de una necesidad concreta, no de un ejercicio técnico. En algún momento decidí dejar de vibecoding y construir algo que resolviera un problema real que tengo cada semana como profesor de inglés: crear exámenes y corregir redacciones lleva tiempo, y gran parte de ese tiempo es mecánico y repetitivo.

El resultado es una pequeña aplicación en Streamlit que usa la API de OpenAI para generar exámenes de inglés adaptados al nivel del alumno y evaluar sus redacciones. No pretende reemplazar el criterio del profesor — pretende encargarse de la parte mecánica para que ese criterio pueda aplicarse donde de verdad importa.

---

## Cómo funciona

La aplicación tiene dos funcionalidades principales.

**Generación de exámenes**: recibe un nivel CEFR y un flag opcional de adaptación para dislexia, rellena una plantilla de prompt y devuelve un examen listo para usar. El modelo tiene instrucciones para generar instrucciones sencillas, sin tareas orales y con cinco preguntas calibradas al nivel seleccionado.

**Corrección de redacciones**: recibe el texto escrito por un alumno, lo evalúa en función del nivel esperado y devuelve una puntuación estructurada de gramática, vocabulario y estructura, junto con un comentario breve de feedback. La respuesta llega en JSON para que la interfaz pueda mostrarla de forma limpia.

Ambas funcionalidades admiten un flag de adaptación para dislexia que ajusta el prompt en consecuencia.

---

## Instalación

Clona el repositorio e instala las dependencias:

```bash
git clone https://github.com/Rcerezo-dev/Exam_creator.git
cd Exam_creator
pip install -r requirements.txt
```

Crea un archivo `.env` en la raíz con tu clave de la API de OpenAI:

```
OPENAI_API_KEY=tu_clave_aqui
```

Ejecuta la aplicación:

```bash
streamlit run app.py
```

---

## Mejoras futuras

La versión actual cubre el flujo principal, pero hay bastante margen para crecer. Algunas direcciones que tienen sentido:

**Mas tipos de tarea.** Ahora mismo la app genera un examen genérico. El siguiente paso natural sería dejar que el profesor especifique qué tipo de ejercicios incluir — comprensión lectora, rellenar huecos, opción múltiple, redacción — y que el modelo construya el examen en consecuencia.

**Foco en gramática y vocabulario.** Poder decirle al modelo "céntrate en el past simple y los verbos irregulares" o "usa vocabulario del tema de medio ambiente" haría la herramienta mucho más útil en contextos reales de aula.

**Exportar a PDF.** El examen ahora vive dentro de la app. Exportarlo como PDF o Word formateado cerraría el hueco entre la generación y el uso real en clase.

**Otras asignaturas.** Los prompts están construidos pensando en inglés, pero la arquitectura es suficientemente general como para soportar otros idiomas o asignaturas con cambios mínimos.

**Historial de alumnos.** Guardar correcciones anteriores con su fecha permitiría a los profesores seguir la evolución a lo largo del tiempo e identificar errores recurrentes en un grupo.
