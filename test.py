import feedparser
from piglow import PiGlow

piglow = PiGlow()

USERNAME="username@gmail.com"
PASSWORD="password"

ledbrightness = 20

###resets lights to off
piglow.all(0)

newmails = int(feedparser.parse("https://" + USERNAME + ":" + PASSWORD + "@mail.google.com/gmail/feed/atom")["feed"]["fullcount"])
if newmails > 0:
  piglow.all(ledbrightness)
