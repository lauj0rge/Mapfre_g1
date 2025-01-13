# Chatbot con IA Generativa y Recuperación Basada en el Conocimiento (RAG)

## Proyecto: Grupo 1 - Compañía de Seguros: Mapfre

### Descripción General
Este proyecto tiene como objetivo desarrollar un chatbot basado en inteligencia artificial generativa y Recuperación Basada en el Conocimiento (RAG) para asistir a una compañía de seguros en la atención al cliente, mejora de procesos internos y optimización de consultas frecuentes. La solución combina modelos generativos avanzados con sistemas de búsqueda para proporcionar respuestas precisas y contextualizadas.

---

### Características Principales

1. **Generación de Lenguaje Natural (NLG):**
   - Uso de modelos avanzados como OpenAI para generar respuestas coherentes y naturales.

2. **Recuperación Basada en el Conocimiento (RAG):**
   - Integración con bases de datos y documentos relevantes de la compañía.
   - Utiliza vectores embebidos para buscar y recuperar información precisa en tiempo real.

3. **Integración con Base de Datos:**
   - Implementación de PostgreSQL para almacenar y recuperar datos estructurados.
   - Uso de PGVector para manejo de embeddings.

4. **Adaptación a Contexto del Cliente:**
   - Capacidad de comprender consultas complejas y proporcionar respuestas adaptadas a las necesidades específicas del usuario.

5. **Escalabilidad y Personalización:**
   - Diseño modular que permite agregar nuevas funcionalidades o ajustar a diferentes líneas de negocio.

---

### Tecnologías Utilizadas

- **Lenguajes de Programación:** Python
- **Frameworks:** LlamaIndex, SQLAlchemy
- **Base de Datos:** PostgreSQL (PGVector para almacenamiento de embeddings)
- **Modelos Generativos:** OpenAI GPT
- **Herramientas:** DBeaver, Pyenv
- **Control de Versiones:** Git y GitHub

---

### Requisitos del Sistema

1. **Sistema Operativo:** macOS, Linux o Windows
2. **Python:** Versión 3.12 o superior
3. **Dependencias:**
   - psycopg2
   - openai
   - llama-index
   - sqlalchemy
   - python-dotenv (opcional para gestión de claves API)
4. **Base de Datos:** PostgreSQL 14 o superior
5. **Conexión a Internet:** Necesaria para interactuar con el modelo generativo

---

### Estructura del Proyecto

```plaintext
Mapfre_g1/
├── datasets/              # Documentos utilizados para entrenar el chatbot
├── index_creator.py       # Script principal para crear el índice
├── create_db.py           # Script para inicializar la base de datos
├── api_key.py             # Archivo para configurar la clave API (opcional)
├── requirements.txt       # Dependencias del proyecto
├── README.md              # Documentación del proyecto
├── env/                   # Variables de entorno (opcional)
```

---


### Contribución

Laura Jorge	
Santiago Esbert	
Pablo Villamaña Río	

