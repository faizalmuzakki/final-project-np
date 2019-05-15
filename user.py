from threading import Thread

class User:
    def __init__(self):
        self.session = None
        Thread.__init__(self)
    
    def run(self, data):
        print self.session
            
    
    def get_auth(self):
        return self.session
    
    def set_auth(self, session):
        self.session = session
