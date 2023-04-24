import socket

def getip(url):
    try:
        results=socket.gethostbyname_ex(url)
    except:
        results=[]
    return results

def display(results):
    output=''
    if(not results):
        for x in results:
            output=output+str(x)+' '
    print(output)
    print()

display(getip(''))
display(getip('www.google.com'))