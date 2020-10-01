import feedparser
import telegram_channel
import data_handler


def poll_titles_from_medium(tickers):
    try:
        feed = feedparser.parse("https://medium.com/feed/@coinbaseblog")
        feed_entries = feed.entries
        for entry in feed.entries:
            blog_post_title = entry.title
            res = [ticker for ticker in tickers if(ticker in blog_post_title)]
            if res:
                symbol = res[0]
                print(f"Found a blog post for symbol: {symbol}")
                print(blog_post_title)
                print()
                telegram_channel.send_message_to_me(f"Found post for symbol {symbol}: \n\n{blog_post_title}")
                return res
        return []
    except Exception as e:
        print(e)
        telegram_channel.send_message_to_me(f"EXCEPTION poll_titles_from_medium():\n{e}")