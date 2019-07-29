import urllib.request

try:                                                     ##for exception handling 
    url=urllib.request.urlopen("https://www.python.org/")
    content=url.read()              ## read the content of url
    url.close()
except urllib.error.HTTPError:      ##if the page is not there then it will give an error
    print("the web page is not found")
    exit()
    
f=open('python.html','wb')        ##open a file and write the data of url
f.write(content)
f.close()
