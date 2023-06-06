import socket
import threading

target="127.0.0.1"
def KILLPORTS():
    def port_scanner(port):
        try:
            soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            soc.connect(target, port)
            print(f'Port {port} is open')
            soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            soc.bind(target, port)
            soc.close()
        except:
            pass
    for port in range(1,5050):
        thread = threading.Thread(target=port_scanner, args=[port])
        thread.start()

KILLPORTS()
#netstat -ano | findstr :{portNumber}
#taskkill /PID {typeyourPIDhere} /F