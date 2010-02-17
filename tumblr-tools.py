# made by Ted Roden... but you can do whatever you want with this.
import urllib, urllib2, sys
from xml.dom import minidom

class TumblrTools(object):
    
    def get_urls_that_you_follow(self, user, password):
        realm = "Twitter API"
        url = "http://www.tumblr.com/statuses/home_timeline.xml?count=200"

        largest_id = 0
        passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
        # this creates a password manager
        passman.add_password(None, url, user, password)
        authhandler = urllib2.HTTPBasicAuthHandler(passman)
        opener = urllib2.build_opener(authhandler)
        urllib2.install_opener(opener)
        try:
            pagehandle = urllib2.urlopen(url)
            dom = minidom.parse(pagehandle)
        except Exception, e:
            if e.code == 401:
                print "Couldn't log you in. Make sure you username and password are correct"
            else:
                print "Some HTTP error!"
            quit()
        cnt = 0
        urls = {}
        for x in dom.getElementsByTagName('user'):
            url = name = False
            for n in x.childNodes:
                if n.nodeName == 'url' and n.firstChild:
                    url = n.firstChild.data
                if n.nodeName == 'name' and n.firstChild:
                    name = n.firstChild.data
                if name and url:
                    urls[url] = name
                    break

        return urls
        
        
if __name__ == "__main__":
    t = TumblrTools()

    username = password = False
    if len(sys.argv) < 3:
        print "You need to call this like so: python %s username password" % sys.argv[0]
        exit()
    else:
        username = sys.argv[1]
        password = sys.argv[2]

    urls = t.get_urls_that_you_follow(username, password)
    output_filename = 'the-people-that-i-follow-on-tumblr.opml'
    try:
        f = open(output_filename, 'w')
        f.write("<?xml version=\"1.0\" encoding=\"utf-8\" ?>\n<opml version=\"1.1\"><head></head>\n<body>\n")
        for x in urls:
            f.write("\t<outline text=\"")
            f.write(urls[x].encode('utf-8').replace("\"", "&quot;"))
            f.write("\" xmlUrl=\"%srss\" />\n" % x)

        f.write('</body>')
        f.close()
    except Exception, e:
        print "Something went wrong!"
        print x
        print e
        quit()
    print "Everything worked, I created a file called \"%s\"" % output_filename
    print "Import that into google reader or whatever"
    
    
    
    
