# Mastodon Echo Chamber Client

Este proyecto es un cliente básico para Mastodon diseñado para identificar y mitigar cámaras de eco, sugiriendo nuevos usuarios y hashtags.

## Instalación

1. Clona este repositorio.
2. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

3. Configura tus credenciales en `config.py`.

4. Ejecuta la aplicación:

    ```bash
    python app.py
    ```

## Funcionalidades

- Publicar un toot.
- Obtener la línea de tiempo pública.
- Detectar cámaras de eco basadas en hashtags repetidos.
- Sugerir nuevos usuarios y hashtags en tendencia.
