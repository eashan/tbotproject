import sys
from twython import Twython

tweetstring = raw_input("Enter Tweet you want to post:")
apiKey = 'eaFxE0NkGr46Dnfs274r9RZD7'
apiSecret = 'OP5UcaEjR38YQS0aK78ngj2qoTgndoU5ljMnqmM76EEIOy7iiS'
accessToken = '717198497267785728-jhLfal4Ii7VcFGt80KlZPQo1LA1aVJj'
accessTokenSecret = 'fvlwbyFn1j4GMuFNXSKVj5aycoQSu1NM9c1TLXgW9TTrZ'

api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)

api.update_status(status=tweetstring)

print "tweeted:" + tweetstring
