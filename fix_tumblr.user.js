// ==UserScript==
// @name           Fix Tumblr
// @namespace      FT
// @author         Ted Roden tedroden@gmail.com
// @description    This fixes tumblr. (This is sooo poorly done, sorry everybody).
// @include        http://tumblr.com/*
// @include        http://www.tumblr.com/*
// ==/UserScript==

// anything else autopost? just added more things to this array and you can auto hide them
var bannedTitles = ['My Top 5 Artists'];

var bannedImages = ['http://assets.tumblr.com/images/reindeer.png',
					'http://assets.tumblr.com/images/blingbling.png',
					'http://assets.tumblr.com/images/santa.png'
				   ];

function handleYourBusiness() {

		var images = document.getElementsByTagName('img');

		for(var y = 0; y < images.length; ++y) {
			for(var n = 0; n < bannedImages.length; ++n) {
				if(images[y].src.indexOf(bannedImages[n]) != -1) {
					images[y].style.display = 'none';
					images[y].parentNode.removeChild(images[y]);
				}
			}
		}

		var posts = document.getElementsByClassName('post');
		for(var i = 0; i < posts.length; ++i) {

			for(var x = 0; x < posts[i].childNodes.length; ++x) {
				if(!posts[i].childNodes[x].className)
					continue;

				if(posts[i].childNodes[x].className == 'post_content') {
					var kids = posts[i].childNodes[x].childNodes;
					for(var m = 0; m < kids.length; ++m) {
						if(!kids[m].className) {
							continue;
						}
						if(kids[m].className.indexOf('post_question') != -1) {
							posts[i].style.display = 'none';
						}
					}

				}
				if(posts[i].childNodes[x].className == 'post_title') {
					for(var n = 0; n < bannedTitles.length; ++n) {
						if(posts[i].childNodes[x].innerHTML.indexOf(bannedTitles[n]) != -1) {
							posts[i].style.display = 'none';
						}
					}
				}

			}
		}
		setTimeout(handleYourBusiness, 500);
	}

if(window.location.hostname.indexOf('tumblr.com') != -1) {
	if(window.location.pathname.indexOf('/dashboard') == 0) {
		handleYourBusiness();
	}
	if(window.location.pathname.indexOf('/tumblupon') == 0) {
		var id = window.location.href.split('/').pop();
		window.location.href = 'http://www.tumblr.com/' + id;
	}
}
