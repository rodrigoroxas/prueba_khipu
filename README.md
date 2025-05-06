# 💸 Khipu API 3.0 - Integración de Pagos (Demo)

Este proyecto es una integración básica de la API de Pagos Instantáneos de **Khipu (v3.0)** utilizando `Flask` como backend y `HTML + JavaScript` como frontend. Está diseñada como prueba técnica para el cargo de **Customer Success** y funciona completamente en modo desarrollador con **DemoBank**.

---

## 📦 Tecnologías usadas

- Python 3
- Flask
- Khipu API 3.0 (con autenticación `x-api-key`)
- HTML / JavaScript
- dotenv

---

## 🚀 ¿Qué hace esta app?

- Permite listar bancos disponibles (incluyendo DemoBank).
- Crea un cobro con Khipu usando la API 3.0.
- Redirige al usuario al link de pago retornado por la API.
- Muestra mensajes de confirmación o error.

---

## 🛠️ Cómo ejecutar el proyecto

### 1. Clona el repositorio

```bash
git clone https://github.com/tu_usuario/khipu-integration-demo.git
cd khipu-integration-demo
```

### 2. Crea un entorno virtual

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instala dependencias

```bash
pip install -r requirements.txt
```

### 4. Configura el entorno

Copia el archivo `.env.example` y renómbralo a `.env`:

```bash
cp .env.example .env
```

Edita el archivo `.env` y agrega tu `x-api-key` de Khipu:

```
KHIPU_API_KEY=tu_api_key_real
```

### 5. Ejecuta la app

```bash
python app.py
```

Abre tu navegador en [http://localhost:5000](http://localhost:5000)

---

## 🖼️ Capturas

![screenshot](https://imgur.com/dsiCQe5)
![screenshot](https://imgur.com/bqQfpAg)
![screenshot](https://imgur.com/nVJ5CI3)
![screenshot](https://imgur.com/0ZjyEgu)
![screenshot](https://imgur.com/3dMdd8r)
![screenshot](https://imgur.com/YkrF105)


---

## ✅ DemoBank

Este proyecto está configurado para funcionar en modo desarrollador usando **DemoBank**, lo que permite probar todo el flujo de cobro sin generar transacciones reales.

---

## 🔒 Seguridad

- El archivo `.env` está ignorado por Git y **no debe subirse** nunca al repositorio.
- No compartas tu `API Key` públicamente.

---

## 📬 Contacto

Desarrollado por **Rodrigo** como parte de un proceso técnico.  
¿Preguntas o sugerencias? Contáctame por LinkedIn o GitHub.
[LinkedIn](https://www.linkedin.com/in/rodrigorojasanalistaprog/)
---

