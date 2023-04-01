# AUDIO PROCESSING EXAMPLES

Demonstrate some audio processing examples.  

## Download some realistic free audiobook content

Goto https://librivox.org/ and download some audio books  

```sh
mkdir -p ./sources/audiobooks/  
curl -vvv -L -o ./sources/audiobooks/christmas_short_works_2008_0812_64kb_mp3.zip http://www.archive.org/download/christmas_short_works_2008_0812/christmas_short_works_2008_0812_64kb_mp3.zip
unzip ./sources/audiobooks/christmas_short_works_2008_0812_64kb_mp3.zip -d ./sources/audiobooks/christmas_short_works_2008_0812_64kb_mp3
```

### RSS Feed download

```sh
mkdir -p ./sources
# get rss feed
curl -s -o ./sources/lnlrss.xml https://latenightlinux.com/feed/mp3
# get first url
FEED_URL=$(xmllint --xpath 'string(//rss/channel/item[1]/enclosure/@url)' --format --pretty 2 ./sources/lnlrss.xml)
# get the file
PODCASTFILE=$(basename $FEED_URL)
curl -s -L -o ./sources/${PODCASTFILE} $FEED_URL
```

## Resources

