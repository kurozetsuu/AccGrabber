import os 
import time


B  = '\033[1;34m'
W  = '\033[0m'    # white (default)
R  = '\033[1;31m' # red
G  = '\033[1;32m' # green bold
O  = '\033[1;33m' # orange
B  = '\033[1;34m' # blue
P  = '\033[1;35m' # purple
C  = '\033[1;36m' # cyan
GR = '\033[1;37m' # gray

os.system("clear")


print'''
	        _             ____           _     _          
	       / \   ___ ___ / ___|_ __ __ _| |__ | |__   ___ _ __
	      / _ \ / __/ __| |  _| '__/ _` | '_ \|  _ \ / _ \ '__|
	     / ___ \ (_| (__| |_| | | | (_| | |_) | |_) |  __/ | 
	    /_/   \_\___\___|\____|_|  \__,_|_.__/|_.__/ \___|_|
                                           Author : ./Ay0ub
	    '''

print(G+"[1] Start ")
print(G+"[2] Exit  ")

option = input(B+"AccGrabber : ")

if option == 1:
	import requests 
	acc = raw_input(G+"[?] Enter username : ")

	print(P+"[*] Checking the username  "+acc+" on : ")

	rfacebook = requests.get("https://www.facebook.com/"+acc)
	rinstagram = requests.get("https://www.instagram.com/"+acc)
	rtwitter = requests.get("https://www.twitter.com/"+acc)
	ryoutube = requests.get("https://www.youtube.com/"+acc)
	rvk = requests.get("https://vk.com/"+acc)
	rlinkedin = requests.get("https://www.linkedin.com/"+acc)
	rblogger = requests.get("https://"+acc+".blogspot.com")
	rwordpress = requests.get("https://"+acc+".wordpress.com")
	rgithub = requests.get("https://www.github.com/"+acc)
	rpinterest = requests.get("https://www.pinterest.com/"+acc)
	rreddit = requests.get("https://www.reddit.com/user/"+acc)
	rtumblr = requests.get("https://"+acc+".tumblr.com")
	rflickr  = requests.get("https://www.flickr.com/photos/"+acc)
	rsteam   = requests.get("https://steamcommunity.com/id/"+acc)
	rvimeo   = requests.get("https://www.vimeo.com/"+acc)
	rsoundcloud = requests.get("https://www.soundcloud.com/"+acc)
	rdisqus     = requests.get("https://www.disqus.com/"+acc)
	rmedium = requests.get("https://medium.com/@"+acc)
	rdevianart = requests.get("https://"+acc+".deviantart.com")
	raboutme = requests.get("https://about.me/"+acc)
	rimgur = requests.get("https://imgur.com/user/"+acc)
	rflipboard = requests.get("https://www.flipboard.com/@"+acc)
	rslideshare = requests.get("https://www.slideshare.net/"+acc)
	rspotify = requests.get("https://open.spotify.com/user/"+acc)
	rscribd = requests.get("https://www.scribd.com/"+acc)
	rbadoo = requests.get("https://www.badoo.com/en/"+acc)
	rpatreon = requests.get("https://www.patreon.com/"+acc)
	rdailymotion = requests.get("https://www.dailymotion.com/"+acc)
	rcashme = requests.get("https://cash.me/"+acc)
	rbehance = requests.get("https://www.behance.net/"+acc)
	rgoodreads = requests.get("https://www.goodreads.com/"+acc)
	rkeybase = requests.get("https://www.keybase.io/"+acc)
	rkongregate = requests.get("https://kongregate.com/accounts/"+acc)
	rlivejournal = requests.get("https://"+acc+".livejournal.com")
	rangellist = requests.get("https://angel.co/"+acc)
	rlastfm = requests.get("https://last.fm/user/"+acc)
	rdribbble = requests.get("https://dribbble.com/"+acc)
	rcodecademy = requests.get("https://www.codecademy.com/"+acc)
	rgravatar = requests.get("https://en.gravatar.com/"+acc)
	rpastebin = requests.get("https://foursquare.com/"+acc)
	rfoursquare = requests.get("https://foursquare.com/"+acc)
	rroblox = requests.get("https://foursquare.com/"+acc)
	rgumroad = requests.get("https://www.gumroad.com/"+acc)
	rnewgrounds = requests.get("https://"+acc+".newgrounds.com")
	rwattpad = requests.get("https://www.wattpad.com/user/"+acc)
	rcanva = requests.get("https://www.canva.com/"+acc)
	rcreativemarker = requests.get("https://creativemarket.com/"+acc)
	rtrakt = requests.get("https://www.trakt.tv/users/"+acc)
	r500px = requests.get("https://500px.com/"+acc)
	rbuzzfeed = requests.get("https://buzzfeed.com/"+acc)
	rtripadvisor = requests.get("https://tripadvisor.com/members/"+acc)
	rhubpages = requests.get("https://"+acc+".hubpages.com/")
	rhouzz = requests.get("https://houzz.com/user/"+acc)
	rblipfm = requests.get("https://blip.fm/"+acc)
	rhackernews = requests.get("https://news.ycombinator.com/user?id="+acc)
	rcodementor = requests.get("https://www.codementor.io/"+acc)
	rreverbnation = requests.get("https://www.reverbnation.com/"+acc)
	rifttt = requests.get("https://www.ifttt.com/p/"+acc)
	rebay = requests.get("https://www.ebay.com/usr/"+acc)
	rslack = requests.get("https://"+acc+".slack.com")
	rtrip = requests.get("https://www.trip.skyscanner.com/user/"+acc)
	rello = requests.get("https://ello.co/"+acc)
	rtripit = requests.get("https://www.tripit.com/people/"+acc+"#/profile/basic-info")
	retsy = requests.get("https://www.etsy.com/shop/"+acc)
	rbasecamp = requests.get("https://"+acc+".basecamphq.com/login")
	rtracky = requests.get("https://tracky.com/user/"+acc)
	rokcupid = requests.get("https://www.okcupid.com/profile/"+acc)
	rbandcamp = requests.get("https://www.bandcamp.com/"+acc)
	rwikipedia = requests.get("https://www.wikipedia.org/wiki/User:"+acc)
	rcontently = requests.get("https://"+acc+".contently.com")
	rbitbucket = requests.get("https://bitbucket.org/"+acc)
	rfotolog = requests.get("https://fotolog.com/"+acc)
	rdesignspiration = requests.get("https://www.designspiration.net/"+acc)


	file = open(acc,"w")
	file.write(acc+" results !\n")
	file.write("\n")
	file.write("\n")


	if (rfacebook.ok) == True:
		print(G+"[+] Facebook           : Found     !   "+"https://www.facebook.com/"+acc)

		file.write("[+] Facebook        : Found     !   "+"https://www.facebook.com/"+acc+"\n")

	elif (rfacebook.ok) == False:
		print(R+"[!] Facebook           : Not found ! ")

	if (rinstagram.ok) == True:
		print(G+"[+] instagram          : Found     !   "+"https://www.instagram.com/"+acc)

		file.write("[+] instagram       : Found     !   "+"https://www.instagram.com/"+acc+"\n")

	elif(rinstagram.ok) == False:
		print(R+"[!] Instagram          : Not found ! ")
		time.sleep(0.1)

	if (rtwitter.ok) == True:
		print(G+"[+] Twitter            : Found     !   "+"https://www.twitter.com/"+acc)

		file.write("[+] Twitter         : Found     !   "+"https://www.twitter.com/"+acc+"\n")

	elif (rtwitter.ok) == False :
		print(R+"[!] Twitter            : Not found ! ")

	if (ryoutube.ok) == True:
		print(G+"[+] Youtube            : Found     !   "+"https://www.youtube.com/"+acc)

		file.write("[+] Youtube         : Found     !   "+"https://www.youtube.com/"+acc+"\n")
	elif (ryoutube.ok) == False:
		print(R+"[!] Youtube            : Not found ! ")

	if (rvk.ok) == True:
		print(G+"[+] Vk                 : Found     !   "+"https://www.vk.com/"+acc)

		file.write("[+] Vk              : Found     !   "+"https://www.vk.com/"+acc+"\n")

	elif (rvk.ok) == False:
		print(R+"[!] Vk                 : Not found ! ")

	if (rlinkedin.ok) == True:
		print(G+"[+] Linkedin           : Found     !   "+"https://www.linkedin.com/"+acc)

		file.write("[+] Linkedin        : Found     !   "+"https://www.linkedin.com/"+acc+"\n")

	elif (rlinkedin.ok) == False :
		print(R+"[!] Linkedin           : Not found ! ")

	if (rblogger.ok) == True:
		print(G+"[+] Blogger            : Found     !   "+"https://"+acc+".blogspot.com")

		file.write("[+] Blogger         : Found     !   "+"https://"+acc+".blogspot.com"+"\n")

	elif (rblogger.ok) == False:
		print(R+"[!] Blogger            : Not found ! ")

	if (rwordpress.ok) == True : 
		print(G+"[+] Wordpress          : Found     !   "+"https://"+acc+".wordpress.com")

		file.write("[+] Wordpress       : Found     !   "+"https://"+acc+".wordpress.com"+"\n")

	elif (rwordpress.ok) == False :
		print("[!] Wordpress            : Not found !")

	if (rgithub.ok) == True:
		print(G+"[+] Github             : Found     !   "+"https://www.github.com/"+acc)
 
		file.write("[+] Github          : Found     !   "+"https://www.github.com/"+acc+"\n")

	elif (rgithub.ok) == False:
		print(R+"[!] Github             : Not found ! ")

	if (rpinterest.ok) == True:
		print(G+"[+] Pinterest          : Found     !   "+"https://www.pinterest.com/"+acc)

		file.write("[+] Pinterest       : Found     !   "+"https://www.pinterest.com/"+acc+"\n")

	elif (rpinterest.ok) == False:
		print(R+"[!] Pinterest          : Not found ! ")

	if (rreddit.ok) == True:
		print(G+"[+] Reddit             : Found     !   "+"https://www.reddit.com/user/"+acc)

		file.write("[+] Reddit          : Found     !   "+"https://www.reddit.com/user/"+acc+"\n")

	elif (rreddit.ok) == False:
		print(R+"[!] Reddit             : Not found ! ")

	if (rtumblr.ok) == True:
		print(G+"[+] Tumblr             : Found     !   "+"https://"+acc+".tumblr.com")

		file.write("[+] Tumblr          : Found     !   "+"https://"+acc+".tumblr.com"+"\n")

	elif (rtumblr.ok) == False:
		print(R+"[!] Tumblr             : Not found ! ")	

	if (rflickr.ok) == True:
		print(G+"[+] Flickr             : Found     !   "+"https://www.flickr.com/photos/"+acc)

		file.write("[+] Flickr          : Found     !   "+"https://www.flickr.com/photos/"+acc+"\n")

	elif (rflickr.ok) == False:
		print(R+"[!] Flickr             : Not found ! ")

	if (rflickr.ok) == True:
		print(G+"[+] Steam              : Found     !   "+"https://www.steamcommunity.com/id/"+acc)

		file.write("[+] Steam           : Found     !   "+"https://www.steamcommunity.co/id/"+acc+"\n")

	elif (rflickr.ok) == False:
		print(R+"[!] Steam              : Not found ! ")

	if (rvimeo.ok) == True:
		print(G+"[+] Vimeo              : Found     !   "+"https://www.vimeo.com/"+acc)

		file.write("[+] Vimeo           : Found     !   "+"https://www.vimeo.com/"+acc+"\n")

	elif (rvimeo.ok) == False:
		print(R+"[!] Vimeo              : Not found ! ")
 
	if (rsoundcloud.ok) == True:
		print(G+"[+] Soundcloud         : Found     !   "+"https://www.soundcloud.com/"+acc)

		file.write("[+] Soundcloud      : Found     !   "+"https://www.soundcloud.com/"+acc+"\n")

	elif (rsoundcloud.ok) == False:
		print(R+"[!] Soundcloud         : Not found ! ")

	if (rdisqus.ok) == True:
		print(G+"[+] Disqus             : Found     !   "+"https://www.disqus.com/"+acc)

		file.write("[+] Disqus          : Found     !   "+"https://www.disqus.com/"+acc+"\n")

	elif (rdisqus.ok) == False:
		print(R+"[!] Disqus             : Not found ! ")

	if (rmedium.ok) == True:
		print(G+"[+] Medium             : Found     !   "+"https://www.medium.com/@"+acc)

		file.write("[+] Medium          : Found     !   "+"https://www.medium.com/@"+acc+"\n")

	elif (rmedium.ok) == False:
		print(R+"[!] Medium             : Not found ! ")

	if (rdevianart.ok) == True:
		print(G+"[+] DevianART          : Found     !   "+"https://"+acc+"devianart.com/")

		file.write("[+] DevianART       : Found     !   "+"https://"+acc+"devianart.com/"+"\n")

	elif (rdevianart.ok) == False:
		print(R+"[!] DevianART          : Not found ! ")

	if (raboutme.ok) == True:
		print(G+"[+] About.me           : Found     !   "+"https://www.about.me/"+acc)

		file.write("[+] About.me        : Found     !   "+"https://about.me/"+acc+"\n")

	elif (raboutme.ok) == False:
		print(R+"[!] About.me           : Not found ! ")

	if (rimgur.ok) == True:
		print(G+"[+] Imgur              : Found     !   "+"https://www.imgur.com/user/"+acc)

		file.write("[+] Imgur           : Found     !   "+"https://www.imgur.me/user/"+acc+"\n")

	elif (rimgur.ok) == False:
		print(R+"[!] Imgur              : Not found ! ")

	if (rflipboard.ok) == True:
		print(G+"[+] Flipboard          : Found     !   "+"https://www.flipboard.com/@"+acc)

		file.write("[+] Flipboard       : Found     !   "+"https://www.flipboard.com/@"+acc+"\n")

	elif (rflipboard.ok) == False:
		print(R+"[!] Flipboard          : Not found ! ")

	if (rslideshare.ok) == True:
		print(G+"[+] Slideshare         : Found     !   "+"https://www.slideshare.net/"+acc)

		file.write("[+] Slideshare      : Found     !   "+"https://www.slideshare.net/"+acc+"\n")

	elif (rslideshare.ok) == False:
		print(R+"[!] Slideshare         : Not found ! ")

	if (rspotify.ok) == True:
		print(G+"[+] Spotify            : Found     !   "+"https://open.spotify.com/user/"+acc)

		file.write("[+] Spotify         : Found     !   "+"https://open.spotify.com/user/"+acc+"\n")

	elif (rspotify.ok) == False:
		print(R+"[!] Spotify            : Not found ! ")

	if (rscribd.ok) == True:
		print(G+"[+] Scribd             : Found     !   "+"https://www.scribd.com/"+acc)

		file.write("[+] Scribd          : Found     !   "+"https://www.scribd.com/"+acc+"\n")

	elif (rscribd.ok) == False:
		print(R+"[!] Scribd             : Not found ! ")

	if (rbadoo.ok) == True:
		print(G+"[+] Badoo              : Found     !   "+"https://www.badoo.com/en/"+acc)

		file.write("[+] Badoo           : Found     !   "+"https://www.badoo.com/en/"+acc+"\n")

	elif (rbadoo.ok) == False:
		print(R+"[!] Badoo              : Not found ! ")

	if (rpatreon.ok) == True:
		print(G+"[+] Patreon            : Found     !   "+"https://www.patreon.com/"+acc)

		file.write("[+] Patreon         : Found     !   "+"https://www.patreon.com/"+acc+"\n")

	elif (rpatreon.ok) == False:
		print(R+"[!] Patreon            : Not found ! ")

	if (rdailymotion.ok) == True:
		print(G+"[+] Dailymotion        : Found     !   "+"https://www.dailymotion.com/"+acc)

		file.write("[+] Dailymotion     : Found     !   "+"https://www.dailymotion.com/"+acc+"\n")

	elif (rdailymotion.ok) == False:
		print(R+"[!] Dailymotion        : Not found ! ")

	if (rcashme.ok) == True:
		print(G+"[+] CashMe             : Found     !   "+"https://www.cash.me/"+acc)

		file.write("[+] CashMe          : Found     !   "+"https://www.cash.me/"+acc+"\n")

	elif (rcashme.ok) == False:
		print(R+"[!] CashMe             : Not found ! ")

	if (rbehance.ok) == True:
		print(G+"[+] Behance            : Found     !   "+"https://www.behance.com/"+acc)

		file.write("[+] Behance         : Found     !   "+"https://www.behance.com/"+acc+"\n")

	elif (rbehance.ok) == False:
		print(R+"[!] Behance            : Not found ! ")

	if (rgoodreads.ok) == True:
		print(G+"[+] GoodReads          : Found     !   "+"https://www.goodreads.com/"+acc)

		file.write("[+] GoodReads       : Found     !   "+"https://www.goodreads.com/"+acc+"\n")

	elif (rgoodreads.ok) == False:
		print(R+"[!] GoodReads          : Not found ! ")

	if (rkeybase.ok) == True:
		print(G+"[+] Keybase            : Found     !   "+"https://www.keybase.io/"+acc)

		file.write("[+] Keybase         : Found     !   "+"https://www.keybase.io/"+acc+"\n")

	elif (rkeybase.ok) == False:
		print(R+"[!] Keybase            : Not found ! ")

	if (rkongregate.ok) == True:
		print(G+"[+] Kongregate         : Found     !   "+"https://kongregate.com/accounts/"+acc)

		file.write("[+] Kongregate      : Found     !   "+"https://kongregate.com/accounts/"+acc+"\n")

	elif (rkongregate.ok) == False:
		print(R+"[!] Kongregate         : Not found ! ")

	if (rlivejournal.ok) == True:
		print(G+"[+] LiveJournal        : Found     !   "+"https://"+acc+".livejournal.com")

		file.write("[+] LiveJournal     : Found     !   "+"https://"+acc+".livejournal.com"+"\n")

	elif (rlivejournal.ok) == False:
		print(R+"[!] LiveJournal        : Not found ! ")


	if (rangellist.ok) == True:
		print(G+"[+] AngelList          : Found     !   "+"https://angel.co/"+acc)

		file.write("[+] AngelList       : Found     !   "+"https://angel.co/"+acc+"\n")

	elif (rangellist.ok) == False:
		print(R+"[!] AngelList          : Not found ! ")

	if (rlastfm.ok) == True:
		print(G+"[+] Last.fm            : Found     !   "+"https://last.fm/user/"+acc)

		file.write("[+] Last.fm         : Found     !   "+"https://last.fm/user/"+acc+"\n")

	elif (rlastfm.ok) == False:
		print(R+"[!] Last.fm            : Not found ! ")

	if (rdribbble.ok) == True:
		print(G+"[+] Dribbble           : Found     !   "+"https://dribbble.com/"+acc)

		file.write("[+] Dribble         : Found     !   "+"https://dribbble.com/"+acc+"\n")

	elif (rdribbble.ok) == False:
		print(R+"[!] Dribbble           : Not found ! ")

	if (rcodecademy.ok) == True:
		print(G+"[+] Codecademy         : Found     !   "+"https://www.codecademy.com/"+acc)

		file.write("[+] Codecademy      : Found     !   "+"https://www.codecademy.com/"+acc+"\n")

	elif (rcodecademy.ok) == False:
		print(R+"[!] Codecademy         : Not found ! ")

	if (rgravatar.ok) == True:
		print(G+"[+] Gravatar           : Found     !   "+"https://en.gravatar.com/"+acc)

		file.write("[+] Gravatar        : Found     !   "+"https://en.gravatar.com/"+acc+"\n")

	elif (rgravatar.ok) == False:
		print(R+"[!] Gravatar           : Not found ! ")

	if (rpastebin.ok) == True:
		print(G+"[+] Pastebin           : Found     !   "+"https://pastebin.com/u/"+acc)

		file.write("[+] Pastebin        : Found     !   "+"https://pastebin.com/u/"+acc+"\n")
 
	elif (rpastebin.ok) == False:
		print(R+"[!] Pastebin           : Not found ! ")

	if (rfoursquare.ok) == True:
		print(G+"[+] Foursquare         : Found     !   "+"https://foursquare.com/"+acc)

		file.write("[+] Foursquare      : Found     !   "+"https://foursquare.com/"+acc+"\n")

	elif (rfoursquare.ok) == False: 
		print(R+"[!] Foursquare         : Not found ! ")

	if (rroblox.ok) == True:
		print(G+"[+] Roblox             : Found     !   "+"https://foursquare.com/"+acc)

		file.write("[+] Roblox          : Found     !   "+"https://foursquare.com/"+acc+"\n")

	elif (rfoursquare.ok) == False:
		print(R+"[!] Roblox             : Not found ! ")

	if (rgumroad.ok) == True:
		print(G+"[+] Gumroad            : Found     !   "+"https://www.gumroad.com/"+acc)

		file.write("[+] Gumroad         : Found     !   "+"https://www.gumroad.com/"+acc+"\n")

	elif (rgumroad.ok) == False:
		print(R+"[!] Gumroad            : Not found ! ")

	if (rnewgrounds.ok) == True:
		print(G+"[+] Newgrounds         : Found     !   "+"https://"+acc+".newgrounds.com")

		file.write("[+] Newgrounds      : Found     !   "+"https://"+acc+".newgrounds.com"+"\n")

	elif (rnewgrounds.ok) == False:
		print(R+"[!] Newgrounds         : Not found ! ")

	if (rwattpad.ok) == True:
		print(G+"[+] Wattpad            : Found     !   "+"https://www.wattpad.com/user/"+acc)

		file.write("[+] Wattpad         : Found     !   "+"https://www.wattpad.com/user/"+acc+"\n")

	elif (rwattpad.ok) == False:
		print(R+"[!] Wattpad            : Not found ! ")

	if (rcanva.ok) == True:
		print(G+"[+] Canva              : Found     !   "+"https://www.canva.com/"+acc)

		file.write("[+] Canva           : Found     !   "+"https://www.canva.com/"+acc+"\n")

	elif (rcanva.ok) == False:
		print(R+"[!] Wattpad            : Not found ! ")


	if (rcreativemarker.ok) == True:
		print(G+"[+] CreativeMarket     : Found     !   "+"https://creativemarket.com/"+acc)

		file.write("[+] CreativeMarket  : Found     !   "+"https://creativemarket.com/"+acc+"\n")

	elif (rcreativemarker.ok) == False:
		print(R+"[!] CreativeMarket     : Not found ! ")

	if (rtrakt.ok) == True:
		print(G+"[+] Trakt              : Found     !   "+"https://www.trakt.tv/users/"+acc)

		file.write("[+] Trakt           : Found     !   "+"https://www.trakt.tv/users/"+acc+"\n")

	elif (rtrakt.ok) == False:
		print(R+"[!] Trakt              : Not found ! ")

	if (r500px.ok) == True:
		print(G+"[+] 500px              : Found     !   "+"https://500px.com/"+acc)

		file.write("[+] 500px           : Found     !   "+"https://500px.com/"+acc+"\n")

	elif (r500px.ok) == False:
		print(R+"[!] 500px              : Not found ! ")

	if (rbuzzfeed.ok) == True:
		print(G+"[+] Buzzfeed           : Found     !   "+"https://buzzfeed.com/"+acc)

		file.write("[+] Buzzfeed        : Found     !   "+"https://buzzfeed.com/"+acc+"\n")

	elif (rbuzzfeed.ok) == False:
		print(R+"[!] Buzzfeed           : Not found ! ")

	if (rtripadvisor.ok) == True:
		print(G+"[+] TripAdvisor        : Found     !   "+"htps://tripadvisor.com/members/"+acc)

		file.write("[+] TripAdvisor     : Found     !   "+"https://tripadvisor.com/members/"+acc+"\n")

	elif (rtripadvisor.ok) == False:
		print(R+"[!] TripAdvisor        : Not found ! ")

	if (rhubpages.ok) == True:
		print(G+"[+] HubPages           : Found     !   "+"https://"+acc+".hubpages.com/")

		file.write("[+] HubPages        : Found     !   "+"https://"+acc+".hubpages.com/"+"\n")

	elif (rhubpages.ok) == False:
		print(R+"[!] HubPages           : Not found ! ")

	if (rhouzz.ok) == True:
		print(G+"[+] Houzz              : Found     !   "+"https://houzz.com/user/"+acc)

		file.write("[+] Houzz           : Found     !   "+"https://houzz.com/user/"+acc+"\n")

	elif (rhouzz.ok) == False:
		print(R+"[!] Houzz              : Not found ! ")

	if (rblipfm.ok) == True:
		print(G+"[+] Blip.fm            : Found     !   "+"https://blip.fm/"+acc)

		file.write("[+] Blip.fm         : Found     !   "+"https://blip.fm/"+acc+"\n")

	elif (rblipfm.ok) == False:
		print(R+"[!] Blip.fm            : Not found ! ")

	if (rhackernews.ok) == True:
		print(G+"[+] HackerNews         : Found     !   "+"https://news.ycombinator.com/user?id="+acc)

		file.write("[+] HackerNews      : Found     !   "+"https://news.ycombinator.com/user?id="+acc+"\n")

	elif (rhackernews.ok) == False:
		print(R+"[!] HackerNews         : Not found ! ")

	if (rcodementor.ok) == True:
		print(G+"[+] Codementor         : Found     !   "+"https://www.codementor.io/"+acc)

		file.write("[+] Codementor      : Found     !   "+"https://www.codementor.io/"+acc+"\n")

	elif (rcodementor.ok) == False:
		print(R+"[!] Codementor         : Not found ! ")

	if (rreverbnation.ok) == True:
		print(G+"[+] ReverbNation       : Found     !   "+"https://www.reverbnation.com/"+acc)

		file.write("[+] ReverbNation    : Found     !   "+"https://www.reverbnation.com/"+acc+"\n")

	elif (rreverbnation.ok) == False:
		print(R+"[!] ReverbNation       : Not found ! ")


	if (rifttt.ok) == True:
		print(G+"[+] IFTTT              : Found     !   "+"https://www.ifttt.com/p/"+acc)

		file.write("[+] IFTTTT          : Found     !   "+"https://www.ifttt.com/p/"+acc+"\n")

	elif (rifttt.ok) == False:
		print(R+"[!] IFTTT              : Not found ! ")

	if (rebay.ok) == True:
		print(G+"[+] Ebay               : Found     !   "+"https://www.ebay.com/usr/"+acc)

		file.write("[+] Ebay            : Found     !   "+"https://www.ebay.com/usr/"+acc+"\n")

	elif (rebay.ok) == False:
		print(R+"[!] Ebay               : Not found ! ")

	if (rslack.ok) == True:
		print(G+"[+] Slack              : Found     !   "+"https://"+acc+".slack.com")

		file.write("[+] Slack           : Found     !   "+"https://"+acc+".slack.com"+"\n")

	elif (rslack.ok) == False:
		print(R+"[!] Slack              : Not found ! ")

	if (rtrip.ok) == True:
		print(G+"[+] Trip               : Found     !   "+"https://www.trip.skyscanner.com/user/"+acc)

		file.write("[+] Trip            : Found     !   "+"https://www.trip.skyscanner.com/user/"+acc+"\n")

	elif (rtrip.ok) == False:
		print(R+"[!] Trip               : Not found ! ")

	if (rello.ok) == True:
		print(G+"[+] Ello               : Found     !   "+"https://ello.co/"+acc)

		file.write("[+] Ello            : Found     !   "+"https://ello.co/"+acc+"\n")

	elif (rello.ok) == False:
		print(R+"[!] Ello               : Not found ! ")

	if (rtripit.ok) == True:
		print(G+"[+] Tripit             : Found     !   "+"https://www.tripit.com/people/"+acc+"#/profile/basic-info")

		file.write("[+] Tripit          : Found     !   "+"https://www.tripit.com/people/"+acc+"#/profile/basic-info"+"\n")

	elif (rtripit.ok) == False:
		print(R+"[!] Tripit             : Not found ! ")

	if (retsy.ok) == True:
		print(G+"[+] Etsy               : Found     !   "+"https://www.etsy.com/shop/"+acc)
 
		file.write("[+] Etsy            : Found     !   "+"https://www.etsy.com/shop/"+acc+"\n")

	elif (retsy.ok) == False:
		print(R+"[!] Etsy               : Not found ! ")

	if (rbasecamp.ok) == True:
		print(G+"[+] Basecaamp          : Found     !   "+"https://"+acc+".basecamphq.com/login")
 
		file.write("[+] Basecamp        : Found     !   "+"https://"+acc+".basecamphq.com/login"+"\n")

	elif (rbasecamp.ok) == False:
		print(R+"[!] Basecamp           : Not found ! ")


	if (rtracky.ok) == True:
		print(G+"[+] Tracky             : Found     !   "+"https://tracky.com/user/"+acc)
 
		file.write("[+] Tracky          : Found     !   "+"https://tracky.com/user/"+acc+"\n")

	elif (rtracky.ok) == False:
		print(R+"[!] Tracky             : Not found ! ")

	if (rokcupid.ok) == True:
		print(G+"[+] OkCupid            : Found     !   "+"https://www.okcupid.com/profile/"+acc)
 
		file.write("[+] OkCupid         : Found     !   "+"https://www.okcupid.com/profile/"+acc+"\n")

	elif (rokcupid.ok) == False:
		print(R+"[!] OkCupid            : Not found ! ")

	if (rbandcamp.ok) == True:
		print(G+"[+] Bandcmp            : Found     !   "+"https://www.bandcamp.com/"+acc)
 
		file.write("[+] Bandcamp        : Found     !   "+"https://www.bandcamp.com/"+acc+"\n")

	elif (rbandcamp.ok) == False:
		print(R+"[!] Bandcamp           : Not found ! ")

	if (rwikipedia.ok) == True:
		print(G+"[+] Wikipedia          : Found     !   "+"https://www.wikipedia.org/wiki/User:"+acc)
 
		file.write("[+] Wikipedia       : Found     !   "+"https://www.wikipedia.org/wiki/User:"+acc+"\n")

	elif (rwikipedia.ok) == False:
		print(R+"[!] Wikipedia          : Not found ! ")

	if (rcontently.ok) == True:
		print(G+"[+] Contently          : Found     !   "+"https://"+acc+".contently.com")
 
		file.write("[+] Contently       : Found     !   "+"https://"+acc+".contently.com"+"\n")

	elif (rcontently.ok) == False:
		print(R+"[!] Contently          : Not found ! ")

	if (rbitbucket.ok) == True:
		print(G+"[+] BitBucket          : Found     !   "+"https://bitbucket.org/"+acc)
 
		file.write("[+] BitBucket       : Found     !   "+"https://bitbucket.org/"+acc+"\n")

	elif (rbitbucket.ok) == False:
		print(R+"[!] BitBucket          : Not found ! ")

	if (rfotolog.ok) == True:
		print(G+"[+] Fotolog            : Found     !   "+"https://fotolog.com/"+acc)
 
		file.write("[+] Fotolog         : Found     !   "+"https://fotolog.com/"+acc+"\n")

	elif (rfotolog.ok) == False:
		print(R+"[!] Fotolog            : Not found ! ")

	if (rdesignspiration.ok) == True:
		print(G+"[+] Designspiration    : Found     !   "+"https://www.designspiration.net/"+acc)
 
		file.write("[+] Designspiration : Found     !   "+"https://www.designspiration.net/"+acc+"\n")

	elif (rdesignspiration.ok) == False:
		print(R+"[!] Designspiration    : Not found ! ")



 

	print(B+"Results saved to : "+acc+".txt")



	
if option == 2:

	os.system("exit")

