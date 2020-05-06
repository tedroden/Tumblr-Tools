This was developed before Tumblr had an API. Probably shouldn't be used anymore.

# Tumblr Tools


## tumblr-tools.py

This file contains a class that allows you to pull out all of the feeds that you're following on tumblr and export them as an OPML file. You can import it into another project or just call it from the command line.

Why would you want to do this? This allows you to export all of the feeds that you follow on tumblr and import them into Google Reader. (just click settings -> import in google reader).

### Running tumblr-tools.py
To run it, download it and run:

 - python tumblr-tools.py email@domain.com p4ssw0rd
 - It will save a file called: the-people-that-i-follow-on-tumblr.opml
 - Import that into google reader.
 
## fix_tumblr.user.js

This is a simple greasemonkey script that does a few things to the tumblr dashboard.

 - Hides the imported last.fm posts
 - Hides the "ask me anything" responses
 - Hides "bling" (which i think are gone anyways)
 - Removes the tumblupon bar if you click a link from the Popular/radar page.
 - It used to hide formspring posts, but nobody uses those anymore (sorry formspring)

More info [here](http://tedroden.tumblr.com/post/385529636/i-wasnt-going-to-post-this-here-because-i-feel), [here](http://tedroden.tumblr.com/post/82887815/just-a-quick-note-i-fixed-tumblr-you-can-now) and [here](http://tedroden.tumblr.com/post/298540614/because-i-hate-fun-i-updated-my-i-fixed-tumblr).

### Install it

If you have [greasemonkey](https://addons.mozilla.org/en-US/firefox/addon/748) for firefox, [greasekit](http://8-p.info/greasekit/) for safari or a recent version of google chrome. Install it by clicking below. Otherwise, get one of those things and come back.

[Click here to install Fix Tumblr](http://github.com/tedroden/Tumblr-Tools/raw/master/fix_tumblr.user.js)

## Author

Made by Ted Roden (@[tedroden](http://twitter.com/tedroden/))
Made in 2010

