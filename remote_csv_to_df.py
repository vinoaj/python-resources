FEED_URL = 'https://yyyy.com/feeds/zzzz.csv'

feed = urllib.request.urlopen(FEED_URL)
csv = feed.read().decode()
df = pd.read_csv(io.StringIO(csv))
print(df.head())
