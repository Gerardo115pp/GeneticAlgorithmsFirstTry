import threading
import subprocess
import os

class ServerRuner:
    
    def __init__(self):
        self.react_server = None
        self.flask_server = None
        self.react_process = None
        self.flask_process = None
    
    def startServer(self):
        self.react_server = threading.Thread(target=self.serveReact)
        self.flask_server = threading.Thread(target=self.startFlaskServer)
        self.react_server.start()
        self.flask_server.start()
        # self.react_process.communicate()[0]
        # self.flask_process.communicate()[0]

    def serveReact(self, build_path='web_client\\build'):
        print('react')
        self.react_process = subprocess.Popen(['serve','-l','5001','-s', build_path], shell=True)
    
    def startFlaskServer(self):
        print('server')
        os.chdir('Server')
        self.flask_process = subprocess.Popen(['python', 'Server.py'],shell=True)
    
if __name__ == "__main__":
    server = ServerRuner()
    server.startServer()