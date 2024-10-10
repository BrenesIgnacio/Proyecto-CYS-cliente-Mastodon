class EchoChamberDetector:
    def __init__(self, feed):
        self.feed = feed

    def detect_echo_chambers(self):
        print("\nAnalyzing the feed for echo chambers...\n")
        hashtag_count = {}
        
        # Contar hashtags en el feed
        for toot in self.feed:
            hashtags = [word for word in toot['content'].split() if word.startswith('#')]
            for hashtag in hashtags:
                hashtag_count[hashtag] = hashtag_count.get(hashtag, 0) + 1

        # Identificar hashtags que aparecen frecuentemente
        echo_hashtags = [tag for tag, count in hashtag_count.items() if count > 1]
        if echo_hashtags:
            print(f"Potential echo chambers detected with these hashtags: {', '.join(echo_hashtags)}\n")
        else:
            print("No echo chambers detected!\n")
