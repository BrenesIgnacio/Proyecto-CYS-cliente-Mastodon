from mastodon import Mastodon
import config

class MastodonClient:
    def __init__(self):
        self.mastodon = None

    def log_in(self):
        print("Logging in to Mastodon...")
        self.mastodon = Mastodon(
            access_token=config.ACCESS_TOKEN,
            api_base_url=config.API_BASE_URL
        )
        print("Login successful!\n")

    def status_post(self, message):
        print(f"Posting toot: {message}")
        self.mastodon.status_post(message)
        print(f"Toot posted: \"{message}\" \n")

    def timeline_public(self):
        print("Fetching public timeline...\n")
        feed = self.mastodon.timeline_public()
        for toot in feed:
            print(f"{toot['account']['acct']}: {toot['content']}")
        return feed
