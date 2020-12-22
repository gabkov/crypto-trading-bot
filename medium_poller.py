import feedparser
import telegram_channel
import data_handler


def poll_titles_from_medium(tickers):
    try:
        feed = feedparser.parse("https://medium.com/feed/@coinbaseblog")
        status_code = feed.status
        if status_code != 200:
            telegram_channel.send_message_to_me(f"Status code for feed was {status_code}.")
            print(f"Status code for feed was {status_code}.")
            return [] 
        for entry in feed.entries:
            blog_post_title = entry.title
            res = [ticker for ticker in tickers if(ticker in blog_post_title)]
            listing = "Coinbase Pro" in blog_post_title
            if res and listing:
                return res
        return []
    except Exception as e:
        print(e)
        telegram_channel.send_message_to_me(f"EXCEPTION poll_titles_from_medium():\n{e}")
