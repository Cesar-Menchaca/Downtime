import requests
import re




#declare varibles
r = requests
urlStatusCodes = {200 : "OK", 400 : "Bad Request", 522 : "Connection Timed Out"}

#declare regex compilers
urlBegin = re.compile(r'http(s)?://[w]{3}[.]', re.IGNORECASE)
urlName = re.compile(r'(\w+)[.]com')

websiteList = []


class website:


    def __init__(self, url):
        #checks to see if url contains "https://www.", and ".com"
        begin = urlBegin.search(url)
        name = urlName.search(url)

        #if url doesm't include ".com", ".edu", etc, then it prints to the user to add it and starts the function again
        if name == None:
            return("URL invalid, please add '.com', '.edu', etc")

        #if "https://www." is not included, then it is automatically added to the url
        if begin == None:
            self.name = name[1]
            self.url = "https://www." + name[0]

        websiteList.append(self)



    def urlStatusCode(self):

        url = self.url
        webInfo = r.get(url)

        return(webInfo.status_code)




youtube = website("youtube.com")
facebook = website("facebook.com")
reddit = website("reddit.com")
#add your url here

for sites in websiteList:

    status = sites.urlStatusCode()
    name = sites.name

    print(name)

    if status in urlStatusCodes:
        print(urlStatusCodes[status])

    else:
        print(status)

    print("\n")
