import feedparser
from piglow import PiGlow

piglow = PiGlow()

USERNAME="username@gmail.com"
PASSWORD="password"

ledbrightness = 20

###resets lights to off
piglow.all(0)

newemails = int(feedparser.parse(https://" + USERNAME + ":" + PASSWORD + "@mail.google.com/gmail/feed/atom")["feed"]["fullcount"])
if newmail > 0:
  piglow.all(ledbrightness)
