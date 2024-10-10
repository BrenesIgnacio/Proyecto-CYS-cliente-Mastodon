from mastodon_client import MastodonClient
from echo_chamber_detector import EchoChamberDetector
from recommendations import recommend_users_and_hashtags

def main():
    # Crear instancia del cliente Mastodon
    client = MastodonClient()

    # Iniciar sesión
    client.log_in()

    # Publicar un toot (opcional)
    client.status_post("¡Hola Mastodon! Explorando la diversidad de contenido.")

    # Obtener el feed público
    feed = client.timeline_public()

    # Detectar cámaras de eco
    detector = EchoChamberDetector(feed)
    detector.detect_echo_chambers()

    # Sugerir nuevos usuarios y hashtags
    recommend_users_and_hashtags(client)

if __name__ == "__main__":
    main()
