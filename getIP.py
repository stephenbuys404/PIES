import socket

def getip(url):
    return socket.gethostbyname_ex(url)

def display(results):
    output=''
    if(results):
        for x in results:
            output=output+str(x)+' '
    print(output)
    print()

display(getip(''))
display(getip('www.google.com'))
