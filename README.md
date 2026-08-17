# Bot de WhatsApp con Playwright

Este es un bot que abre WhatsApp Web y envia un mensaje a un numero de telefono.

## Requisitos

- Python 3.11 o superior
- Playwright
- python-dotenv

## Como funciona

1. Lee el numero de telefono desde el archivo .env.
2. Abre WhatsApp Web con un navegador de Chromium.
3. En la primera ejecucion pide escanear el codigo QR para iniciar sesion.
4. La sesion queda guardada en la carpeta auth, asi no vuelve a pedir el QR.
5. Entra al chat del numero y envia el mensaje.

## Configuracion

Crea un archivo `.env` en la raiz del proyecto con el numero de telefono al que quieres enviar el mensaje:

```
PHONE_NUMBER=+58XXXXXXXXXX
```

El archivo .env no se sube al repositorio porque esta en el .gitignore.

## Instalacion

Crea un entorno virtual e instala las dependencias:

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Instala el navegador de Playwright:

```
playwright install chromium
```

## Ejecucion

```
python app.py
```

Tambien puedes usar el archivo `run.bat` en Windows, que ejecuta el bot y no cierra la consola al terminar.

## Notas

- El mensaje que se envia esta definido en app.py.
- Si la sesion caduca, borra la carpeta auth y vuelve a escanear el QR.