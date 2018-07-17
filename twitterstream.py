from tweepy import Stream
from tweepy import OAuthhandler
from tweepy.streaming import StreamListener

ckey = '9zycxff0BoAjQ6fqRltbKEIz3'
csecret = ' J2pdx6SpacKpuTO8iGPZkeksNTxPVvONwpCZ1MjEnWnGF3kSOU'
atoken= ' 2587870818-x1EvLkERGaUznnFRDnWweQahW4h7guI6TUZ1jk1'
asecret= ' osYGTToizX3gXoCXEi39pbIsksLNm25HlhDwu0LpgxvC1'

class Listener(StreamListener):
    def on_data(self,data):
        print(data)
        return True

    def on_error(self,status):
        print(status)

auth = OAuthhandler(ckey,csecret)
auth.set_acces_token(atoken,asecret)
twitterstream = stream(auth,Listener())
twitterstream.filter(['BJP'])

    
