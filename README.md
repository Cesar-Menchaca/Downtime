# Downtime
Checks if a website is down or not


I'll add more instructions once I make more modifications to the code. By default, it checks if Youtube, Reddit, and Facebook. If you want to check more websites, you can add the URL in the code below the three default URLs, as shown below.


youtube = website("youtube.com")
facebook = website("facebook.com")
reddit = website("reddit.com")
#add your url here

You don't need to add "https://www.", the code checks if it is included so that the request is successful. However, it must include ".com" in the end, or else you'll get a warning. Right now, it only supports ".com", so website.edu won't work as well, but that will be updated.
