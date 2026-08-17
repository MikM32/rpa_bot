# TAREA - Bot de WhatsApp con Playwright

## Objetivo

Crear un bot que envie un mensaje por WhatsApp Web indicando que la tarea fue finalizada.

## Requisitos

### 1. Mensaje a enviar

El bot debe enviar un solo mensaje:

```
Tarea finalizada.
```

### 2. Persistencia de sesion (IMPORTANTE)

La primera ejecucion pide escanear el QR. Las siguientes no deben pedirlo. Para eso se guarda y carga la sesion de Playwright:

- Si existe la sesion guardada, cargarla y saltar el QR.
- Si no existe, mostrar el QR, escanear, y al cerrar guardar la sesion.

### 3. Gestion del proyecto con PDM

El proyecto debe manejarse con PDM.

### 4. Ejecucion

El proyecto debe incluir un .bat que ejecute el bot sin cerrar la consola al finalizar.

### 5. Entrega

- Subir el proyecto a un repositorio publico en GitHub.
- Compartir el link del repo.

## Criterios de evaluacion

- El bot envia el mensaje correctamente.
- La sesion se persiste (no pide QR en la segunda ejecucion).
- El proyecto se gestiona con PDM.
- El .bat funciona.
- El repo esta en GitHub y es accesible.